l,m,n,o=map(int,raw_input().split())
s=" NE WS"
while 1:a,b=min(max(o-m,-1),1),min(max(n-l,-1),1);print(s[a]+s[3+b]).strip();o-=a;n-=b