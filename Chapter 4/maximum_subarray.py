def maximum_subarray_crossing(a, low, mid, high):
    maxSumLeft = None
    maxLeft = low

    currentSum = 0
    for i in range(mid - 1, low - 1, -1):
        currentSum += a[i]

        if maxSumLeft == None or currentSum > maxSumLeft:
            maxSumLeft = currentSum
            maxLeft = i


    maxSumRight = None
    maxRight = high

    currentSum = 0
    for i in range(mid, high):
        currentSum += a[i]

        if maxSumRight == None or currentSum > maxSumRight:
            maxSumRight = currentSum
            maxRight = i

    return (maxLeft, maxRight + 1, maxSumLeft + maxSumRight)

def maximum_subarray(a, low, high):
    if high - low == 1:
        return (low, high, a[low])
    else:
        mid = (low + high) // 2
        left = maximum_subarray(a, low, mid)
        right = maximum_subarray(a, mid, high)
        cross = maximum_subarray_crossing(a, low, mid, high)

        if left[2] >= right[2] and left[2] >= cross[2]:
            return left
        elif right[2] >= left[2] and right[2] >= cross[2]:
            return right
        else:
            return cross

def naive_maximum_subarray(a):
    maxLeft = 0
    maxRight = len(a)
    maxSum = None

    for i in range(len(a)):
        for j in range(i + 1, len(a) + 1):
            currentSum = sum(a[i:j])
            if maxSum == None or currentSum > maxSum:
                maxSum = currentSum
                maxLeft = i
                maxRight = j
    
    return (maxLeft, maxRight, maxSum)

def linear_maximum_subarray(a):
    maxLeft = 0
    maxRight = 1
    maxSum = a[0]

    currentSum = a[0]

    replacerSum = a[0]
    replacerStart = 0
    replacerEnd = 1

    for i in range(1, len(a)):
        diff = maxSum - currentSum

        if diff <= a[i]:
            # Extend
            maxRight = i + 1
            maxSum += a[i] - diff

            currentSum += a[i]
        else:
            # Omit
            currentSum += a[i]

        # Update replacer
        replacerSum += a[i]
        replacerEnd += 1

        if replacerSum < a[i]:
            replacerStart = i
            replacerSum = a[i]

        if replacerSum > maxSum:
            # Override
            maxLeft = replacerStart
            maxRight = replacerEnd
            maxSum = replacerSum

            currentSum = maxSum

    return (maxLeft, maxRight, maxSum)

def shortest_linear_maximum_subarray(a):
    maxLeft = 0
    maxRight = 1
    maxSum = a[0]

    currentSum = a[0]

    replacerSum = a[0]
    replacerStart = 0

    for i in range(1, len(a)):
        diff = maxSum - currentSum

        if diff <= a[i]:
            # Extend
            maxRight = i + 1
            maxSum += a[i] - diff

        currentSum += a[i]

        # Update replacer
        replacerSum = max(replacerSum + a[i], a[i])
        if replacerSum == a[i]:
            replacerStart = i

        if replacerSum > maxSum:
            # Override
            maxLeft = replacerStart
            maxRight = i + 1
            currentSum = maxSum = replacerSum

    return (maxLeft, maxRight, maxSum)
