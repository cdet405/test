# 20240226 CD convert json files to ndjson 
import os
from os import error
import json


def convert_json_to_ndjson(indir, infile, outdir=None, outfile=None):
    if not outdir:
      outdir = indir
    if str(outfile).endswith('.json'):
      if outfile == infile:
        outfile = f"nd_{outfile}"
    else:
      outfile = f"nd_{infile}.json"
    inpath = os.path.join(indir, infile)
    outpath = os.path.join(outdir,outfile) 
    try:
      with open(inpath, 'rb') as rf:
        data = json.load(rf)
    except FileNotFoundError as fnfe:
      print('FILE %s NOT FOUND! \n ERROR MSG: %s' % (infile, fnfe)
    result = [json.dumps(record) for record in data]
    with open(outpath, 'w') as wf:
          for i in result:
              wf.write(i+'\n')
    print('converted %s to %s' % (infile, outfile)


        
def main():
    print('starting...')
    convert_json_to_ndjson('/path/', 'example.json', '/path2/', 'output.json')
    print('done')
        
  
