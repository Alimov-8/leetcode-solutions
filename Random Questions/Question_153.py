class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If list empty it returns -1
        if len(nums) == 0: 
            return -1
        
        if len(nums) == 1:
            return nums[0]

        lo, hi = 0, len(nums) - 1

        while lo <= hi: 
            mid = (lo + hi) // 2
            mid_number = nums[mid]

            # Uncomment the next line for logging the values and fixing errors.
            # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

            if mid >= lo and mid_number < nums[mid-1]:
                    return nums[mid]

            elif mid_number > nums[hi]:
                # Answer lies in the right half
                lo = mid + 1

            else:
                # Answer lies in the left half
                hi = mid - 1
                
        return 0
