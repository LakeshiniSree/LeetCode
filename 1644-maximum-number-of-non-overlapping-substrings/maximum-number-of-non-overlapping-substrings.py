from typing import List


class Solution:
    def maxNumOfSubstrings(
        self,
        s: str
    ) -> List[str]:

        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Step 1: first and last occurrence.
        for i, ch in enumerate(s):

            c = ord(ch) - ord('a')

            first[c] = min(first[c], i)
            last[c] = i

        def get_right(L):

            R = last[
                ord(s[L]) - ord('a')
            ]

            i = L

            while i <= R:

                c = (
                    ord(s[i]) -
                    ord('a')
                )

                # This character already appeared
                # before our candidate started.
                if first[c] < L:
                    return -1

                # Include all occurrences
                # of this character.
                R = max(R, last[c])

                i += 1

            return R

        intervals = []

        # Step 2: generate minimal valid intervals.
        for c in range(26):

            if first[c] == n:
                continue

            L = first[c]
            R = get_right(L)

            if R != -1:
                intervals.append((L, R))

        # Earliest ending first.
        # If endings tie, larger L = shorter interval.
        intervals.sort(
            key=lambda x: (
                x[1],
                -x[0]
            )
        )

        ans = []

        last_end = -1

        # Step 3: interval scheduling.
        for L, R in intervals:

            if L > last_end:

                ans.append(
                    s[L:R + 1]
                )

                last_end = R

        return ans