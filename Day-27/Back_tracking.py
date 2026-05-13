def permutations(nums):
    result = []

    def Back_track(path, used):
        # Base condition
        if len(path) == len(nums):
            result.append(path[:])   # store copy
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            # Choose
            path.append(nums[i])
            used[i] = True

            # Explore
            Back_track(path, used)

            # Un-choose (Backtrack)
            path.pop()
            used[i] = False

    Back_track([], [False] * len(nums))
    return result


nums = [1, 2, 3, 4]
print(permutations(nums))