#!/usr/bin/env python3
# realistic sample - non destructive
import argparse, base64, hashlib, json, random, time
def encode_b64(s): return base64.b64encode(s.encode()).decode()
def md5(s): return hashlib.md5(s.encode()).hexdigest()
def demo(n=5):
    out=[]
    for i in range(n):
        s=f"demo-{int(time.time())}-{random.randint(1000,9999)}"
        out.append({"in":s,"b64":encode_b64(s),"md5":md5(s)})
    return out
def main():
    p=argparse.ArgumentParser()
    p.add_argument("action",choices=["demo","encode","md5"])
    p.add_argument("value",nargs="?",default="")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    if args.action=="demo":
        out=demo()
    elif args.action=="encode":
        out=encode_b64(args.value)
    else:
        out=md5(args.value)
    if args.json:
        print(json.dumps(out,indent=2,ensure_ascii=False))
    else:
        print(out)
if __name__=="__main__":
    main()
