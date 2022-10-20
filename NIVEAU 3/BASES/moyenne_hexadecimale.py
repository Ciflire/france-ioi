import sys
import math

def main():
   nbEntrees = int(sys.stdin.readline(),base =16)
   res = 0
   for i in range(nbEntrees):
      res += int(sys.stdin.readline(), base =16)
   sys.stdout.write("%X" % math.floor(res/nbEntrees))
  
   

main()