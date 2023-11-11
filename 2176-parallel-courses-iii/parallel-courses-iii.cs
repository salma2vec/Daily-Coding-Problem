public class Solution
{
    public int MinimumTime(int n, int[][] relations, int[] time)
    {
        Dictionary<int, List<int>> graph = new Dictionary<int, List<int>>();
        int[] inDegree = new int[n + 1];
        int[] dist = new int[n + 1];

        for (int i = 1; i <= n; i++)
        {
            graph[i] = new List<int>();
        }

        foreach (var relation in relations)
        {
            graph[relation[0]].Add(relation[1]);
            inDegree[relation[1]]++;
        }

        Queue<int> queue = new Queue<int>();

        for (int i = 1; i <= n; i++)
        {
            dist[i] = time[i - 1];
            if (inDegree[i] == 0)
            {
                queue.Enqueue(i);
            }
        }

        int maxDist = 0;

        while (queue.Count > 0)
        {
            int course = queue.Dequeue();
            foreach (var nextCourse in graph[course])
            {
                dist[nextCourse] = Math.Max(dist[nextCourse], dist[course] + time[nextCourse - 1]);
                inDegree[nextCourse]--;
                if (inDegree[nextCourse] == 0)
                {
                    queue.Enqueue(nextCourse);
                }
            }
            maxDist = Math.Max(maxDist, dist[course]);
        }

        return maxDist;
    }
}
