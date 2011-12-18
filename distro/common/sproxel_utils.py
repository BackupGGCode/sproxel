import sproxel
from zipfile import *
import json


CUR_VERSION=1


def save_project(filename, proj):
  # gather layers
  layers=[]
  for spr in proj.sprites:
    for l in spr.layers:
      if l not in layers: layers.append(l)

  # prepare metadata
  meta={}
  meta['version']=CUR_VERSION

  meta['layers']=[
    dict(name=l.name, offset=l.offset, visible=l.visible,
      palette = proj.palettes.index(l.palette) if l.palette!=None else -1)
    for l in layers]

  meta['sprites']=[
    dict(name=s.name, layers=[layers.index(l) for l in s.layers], curLayer=s.curLayerIndex)
    for s in proj.sprites]

  meta['palettes']=[
    dict(name=p.name, colors=p.colors)
    for p in proj.palettes]

  meta['mainPalette']=proj.palettes.index(proj.mainPalette)

  # write zip file
  with ZipFile(filename, 'w', ZIP_DEFLATED) as zf:
    zf.writestr('metadata.json', json.dumps(meta, sort_keys=True, indent=2))
    for i, l in enumerate(layers): zf.writestr('%04d.png' % i, l.toPNG())

  return True


def load_project(filename):
  prj=sproxel.Project()

  with ZipFile(filename, 'r') as zf:
    meta=json.loads(zf.read('metadata.json'))

    # load palettes
    palettes=[]
    for mp in meta['palettes']:
      p=sproxel.Palette()
      p.name=mp['name']
      p.colors=[tuple(c) for c in mp['colors']]
      palettes.append(p)

    prj.palettes=palettes

    try:
      prj.mainPalette=palettes[meta['mainPalette']]
    except IndexError:
      try:
        prj.mainPalette=palettes[0]
      except IndexError:
        prj.mainPalette=sproxel.Palette()

    # load layers
    layers=[]
    for i, ml in enumerate(meta['layers']):
      l=sproxel.layer_from_png(zf.read('%04d.png' % i),
        prj.palettes[ml['palette']] if ml['palette']>=0 else None)
      l.name   =ml['name'   ]
      l.offset =tuple(ml['offset'])
      l.visible=ml['visible']
      print 'layer', i, 'type', l.dataType
      layers.append(l)

    # load sprites
    sprites=[]
    for ms in meta['sprites']:
      s=sproxel.Sprite()
      s.name=ms['name']
      for i, li in enumerate(ms['layers']):
        l=layers[li]
        s.insertLayerAbove(i, l)
      s.curLayerIndex=ms['curLayer']
      sprites.append(s)

    prj.sprites=sprites

  #print prj.sprites
  return prj
