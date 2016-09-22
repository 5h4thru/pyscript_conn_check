
import sys
import requests

def filereader(domains, subdomains):
   global dom_list
   global subdom_list
   global lens

   with open(domains, 'r') as f:
      dom_list = []
      for line in f:
         dom_list.append(line.rstrip("\n"))

   with open(subdomains, 'r') as f:
      subdom_list = []
      for line in f:
         subdom_list.append(line.rstrip("\n"))

   print("dom_list:", dom_list)
   print("subdom_list:",subdom_list)
   
   lens = []
   with open(subdomains, 'r') as f:
      lens.append(len(f.readlines()))
   with open(domains, 'r') as f:
      lens.append(len(f.readlines()))
   
def connector():   
   
   for i in range(0, lens[0]):
      for j in range(0, lens[1]):
         try:
            url = "http://"+subdom_list[i]+"."+dom_list[j]+":80"  
            response = requests.get(url)
            if (response.status_code == 200):
               print("Connection Established to -->",url)
               print("Headers:", response.headers['server']) 
         except: 
            print("Connection Aborted to the peer URL:",url)

if __name__ == "__main__":
   try:
      domains = str(sys.argv[1])
      subdomains = str(sys.argv[2])
      filereader(domains, subdomains)
      connector()

   except:
      print("Usage: connect.py domains.txt subdomains.txt")

