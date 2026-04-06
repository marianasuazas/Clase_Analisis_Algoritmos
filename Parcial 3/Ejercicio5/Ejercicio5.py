def canPartition(nums):
    total = sum(nums)
    
    # Si es impar, no se puede dividir
    if total % 2 != 0:
        return False
    
    target = total // 2
    
    # DP: dp[i] = puedo formar suma i
    dp = [False] * (target + 1)
    dp[0] = True  # siempre puedo formar 0
    
    for num in nums:
        # recorrer hacia atrás (clave)
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

nums = [1,2,3,5]
respuesta = canPartition(nums)
print(respuesta)