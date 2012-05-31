#!/usr/bin/env python

import re, sys

def startswith(line=""):
# these need some word-boundary condition, but \b isn't working
ctrlstart = '\s*(function|if|while|for|switch)'
ctrlcont = '\s*(elseif|else|case|catch|otherwise)'
ctrlend = '\s*(end|endfunction|endif|endwhile|endfor|endswitch)'
match = re.match(ctrlstart, line)
if ( match != None ) :
  return ['start',  match.group(0)]
  match=re.match(ctrlcont, line)
  if ( match!=None ) :
    return ['cont',  match.group(0)]
    match=re.match(ctrlend, line)
    if ( match!=None ) :
      return ['end',  match.group(0)]
    else :
      return [False,  None]
      
      def main( filelist = list() ) :
      for filename in filelist:
        nextindent = 0
        indentmult = 2
        file = open(filename, 'r')
        filelines = file.readlines()
        for ind in range(0, len(filelines)) :
          indentlevel = nextindent
          match = startswith(filelines[ind])
          if match[0] == 'start' :
            nextindent += 1
            elif match[0] == 'cont' :
            indentlevel -= 1
            elif match[0] == 'end' :
            indentlevel -= 1
            nextindent -= 1
            elif match[0] == False :
            nextindent = indentlevel
            filelines[ind] = ' '*indentlevel*indentmult + filelines[ind].lstrip().rstrip() +'\n'
            file.close()
            outfile = open(filename, 'w')
            outfile.writelines(filelines)
            outfile.close()
            
            args = []
            for arg in sys.argv[1:] :
              args += [str(arg)]
              main(args)
              
