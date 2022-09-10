
bool isBadVersion(int n);

class Solution
{
public:
    int firstBadVersion(int n)
    {
        long low = 0, high = n;
        while (low <= high)
        {
            long mid = (low + high) / 2;
            if (isBadVersion(mid) && !isBadVersion(mid - 1))
            {
                return mid;
            }
            else if (isBadVersion(mid) && isBadVersion(mid - 1))
            {
                high = mid - 1;
            }
            else
            {
                low = mid + 1;
            }
        }
        return 0;
    }
};
