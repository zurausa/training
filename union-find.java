

public class Main{
    private List<Integer> parent;
    private List<Integer> r;

    public void main(String[] args){
        int n = System.in.readline();
        int m = System.in.readline();
        List<Pair> xList = new ArrayList<>();
        for(int i=0;i<m;i++){
            xList.add(new Pair.initialize(System.in.readline(),System.in.readline(),System.in.readline()));
        }
        parent = new ArrayList<>();
        r = new ArrayList<>();
        List<Integer> pairList;
        int b,c;

        for(int i=0;i<m;i++){
            pairList = xList[i];
             b = pairList[1];
             c = pairList[2];
            if pairList[0] == 0 && find(b) != find(c) union(b,c);
            else if(pairList[0] == 1) conf(b,c);
        }
    }

    private int find(int x){
        if(p[x] != x) p[x] = find(x);
        return p[x];
    }

    private void union(int x,int y){
        x = find(x);
        y = find(y);
        if r[y] > r[x]{
            int tmp = x;
            x = y;
            y = tmp;
        }
        p[y] = x;
        r[x] += r[x] == r[y]
    }

    private void conf(int x,int y){
        if find(x) == find(y) print("Yes");
        else print("No");
    }
}

public class Pair(){
    private int x;
    private int y;
    private int z;
    public void initialize(int x,int y,int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
    
    public List<Integer> getPair(){
        List<Integer> resList = new ArrayList<>();
        resList.add(this.x);
        resList.add(this.y);
        resList.add(this.z);
        return resList;
    }
}