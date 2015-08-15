import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class PrimMSTSub {
  public static class Edge {
    private int x,y,r;

    public Edge(int x, int y, int r) {
      this.x = x;
      this.y = y;
      this.r = r;
    }

    public String toString() {
      return "(" + x + "," + y + "," + r + ")";
    }

    public int getR() {
      return r;
    }
  }

  public static class Graph {
    private Map<Integer, Set<Edge>> edges = new HashMap<>();
    private int n;

    public Graph(int n, Iterable<Edge> edges) {
      this.n = n;
      for (Edge e : edges) {
        if (!this.edges.containsKey(e.x)) {
          this.edges.put(e.x, new HashSet<>());
        }
        this.edges.get(e.x).add(e);
      }
    }

    public Iterable<Edge> getMST(Integer src) {
      List<Edge> mst = new ArrayList<>();
      Set<Integer> remaining = IntStream.rangeClosed(1, this.n).boxed().collect(Collectors.toSet());
      remaining.remove(src);
      Queue<Edge> q = new PriorityQueue<>(Comparator.comparing(Edge::getR));
      q.addAll(this.edges.get(src));

      while(!q.isEmpty()) {
        Edge e = q.poll();
        if (remaining.contains(e.y)) {
          mst.add(e);
          remaining.remove(e.y);
          q.addAll(this.edges.get(e.y));
        }
      }

      return mst;
    }
  }

  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    int m = in.nextInt();
    List<Edge> edges = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      int x = in.nextInt();
      int y = in.nextInt();
      int r = in.nextInt();
      edges.add(new Edge(x,y,r));
      edges.add(new Edge(y,x,r));
    }
    Graph g = new Graph(n, edges);
    int src = in.nextInt();

    int mstSum = 0;
    for (Edge e : g.getMST(src)) {
      mstSum += e.r;
    }
    System.out.println(mstSum);
  }
}
