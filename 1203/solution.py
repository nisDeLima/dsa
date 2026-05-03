class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # =====================================================================
        # STEP 0 — BUILD GROUP BUCKETS
        #
        # group_items[g] will store a list of all items that belong to group g.
        #
        # Items with a valid group (>= 0) are placed normally.
        # Items with group == -1 are assigned a unique artificial group using
        # index (item + 2). This ensures each ungrouped item behaves as its own
        # independent group when performing dependency checks.
        #
        # The array is sized n+2 so "item+2" is always in range.
        # =====================================================================
        group_items = [[] for _ in range(n + 2)]

        for item in range(n):
            if group[item] != -1:
                group_items[group[item]].append(item)
            else:
                group_items[item + 2].append(item)

        # =====================================================================
        # STEP 1 — DFS TOP SORT INSIDE A SINGLE GROUP
        #
        # The goal here is to order items *within* one group so that all
        # internal dependencies are respected.
        #
        # Only dependencies between items in the same group are considered.
        # Dependencies pointing outside the group are ignored at this stage,
        # because cross-group ordering is handled later.
        #
        # Returns:
        #   - True if the group has no cycles
        #   - False if a cycle is found (and sorting is impossible)
        #
        # The result is collected in sorted_group.
        # =====================================================================
        def sort_group(items, sorted_group):
            avail_items = set(items)   # items in this group
            added = set()              # items already placed in sorted order
            checking = set()           # recursion stack for cycle detection

            def dfs(item):
                # If the item is currently being visited, a cycle exists
                if item in checking:
                    return False
                # If already sorted, no need to revisit
                if item in added:
                    return True

                checking.add(item)

                # Visit dependencies that also belong to this group
                for dep in beforeItems[item]:
                    if dep in avail_items:
                        if not dfs(dep):
                            return False

                checking.remove(item)

                # After dependencies are resolved, append this item
                added.add(item)
                sorted_group.append(item)
                return True

            # Run DFS for every item in this group
            for item in items:
                if not dfs(item):
                    return False

            return True

        # =====================================================================
        # STEP 2 — SORT ITEMS WITHIN EACH GROUP
        #
        # Every group is processed independently using the DFS-based top sort.
        #
        # If any group contains a dependency cycle, the entire problem
        # is unsolvable and returns an empty list.
        # =====================================================================
        for idx, items in enumerate(group_items):
            sorted_group = []
            if not sort_group(items, sorted_group):
                return []
            group_items[idx] = sorted_group

        # =====================================================================
        # STEP 3 — GLOBAL DFS OVER GROUPS (INDIRECTLY VIA ITEMS)
        #
        # Now that each group has its internal order fixed,
        # the next step is to order groups relative to each other.
        #
        # The DFS below:
        #   - Ensures inter-group dependencies are respected
        #   - When a group is ready, the entire group is appended at once
        #
        # This DFS operates at the item level but emits whole groups.
        # =====================================================================
        result = []
        added = set()       # items already added globally
        checking = set()    # items currently in recursion (cycle detection)

        def dfs(item):
            # Cycle check
            if item in checking:
                return False
            # If already handled, nothing to do
            if item in added:
                return True

            # Determine which group this item belongs to
            if group[item] == -1:
                local_items = group_items[item + 2]
            else:
                local_items = group_items[group[item]]

            checking.add(item)

            # Before outputting this group, ensure all cross-group
            # dependencies are resolved.
            #
            # For each item in this group:
            #   for each dependency:
            #       if dependency is OUTSIDE this group,
            #       we must recursively process it first.
            for i in local_items:
                for dep in beforeItems[i]:
                    if dep not in local_items:
                        if not dfs(dep):
                            return False

            checking.remove(item)

            # At this point, the group can be safely appended.
            # All dependencies are satisfied.
            for i in local_items:
                result.append(i)
                added.add(i)

            return True

        # =====================================================================
        # STEP 4 — TRY TO DFS FROM EVERY ITEM
        #
        # This ensures all connected components are explored.
        # If any part has a cycle, sorting is impossible.
        # =====================================================================
        for item in range(n):
            if not dfs(item):
                return []

        return result

