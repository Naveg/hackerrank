import java.util.*;

public class KruskalMSTSub {
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

    public Iterable<Edge> getMST() {
      List<Edge> mst = new ArrayList<>();

      Queue<Edge> q = new PriorityQueue<>(Comparator.comparing(Edge::getR));
      for (Set<Edge> es : edges.values()) {
        q.addAll(es);
      }

      Set<Set<Integer>> components = new HashSet<>();
      for (int i = 1; i <= n; i++) {
        Set<Integer> s = new HashSet<>();
        s.add(i);
        components.add(s);
      }

      while(components.size() > 1 && !q.isEmpty()) {
        Edge e = q.poll();
        Set<Integer> s1 = null, s2 = null;
        for (Set<Integer> s : components) {
          if (s.contains(e.x)) {
            s1 = s;
          }
          if (s.contains(e.y)) {
            s2 = s;
          }
        }

        if (!s1.equals(s2)) {
          mst.add(e);
          s1.addAll(s2);
          s2.clear();
          components.removeIf(Set::isEmpty);
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
    }
    Graph g = new Graph(n, edges);

    int mstSum = 0;
    for (Edge e : g.getMST()) {
      mstSum += e.r;
    }
    System.out.println(mstSum);
  }
}
