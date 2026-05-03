class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Edge case: can't have primes below 2
        if right < 2:
            return [-1, -1]
        
        # Step 1: Create a list to track which numbers are prime
        # Start by assuming everything is prime
        is_prime = [True] * (right + 1)
        is_prime[0] = False  # 0 is not prime
        is_prime[1] = False  # 1 is not prime
        
        # Step 2: Sieve of Eratosthenes - mark all composite numbers
        # We only need to check up to square root of right
        limit = int(right ** 0.5) + 1
        
        for current_number in range(2, limit):
            # If this number is still marked as prime
            if is_prime[current_number]:
                # Mark all its multiples as NOT prime
                # Start from current_number squared (optimization!)
                first_multiple = current_number * current_number
                
                # Mark every multiple of current_number
                multiple = first_multiple
                while multiple <= right:
                    is_prime[multiple] = False
                    multiple += current_number
        
        # Step 3: Collect all primes in our range [left, right]
        primes_in_range = []
        start = max(2, left)  # Don't check below 2 or below left
        
        for number in range(start, right + 1):
            if is_prime[number]:
                primes_in_range.append(number)
        
        # Step 4: Check if we have at least 2 primes
        if len(primes_in_range) < 2:
            return [-1, -1]
        
        # Step 5: Find the pair with minimum distance
        smallest_distance = float('inf')
        closest_pair = [-1, -1]
        
        # Check consecutive primes
        for i in range(1, len(primes_in_range)):
            previous_prime = primes_in_range[i - 1]
            current_prime = primes_in_range[i]
            distance = current_prime - previous_prime
            
            if distance < smallest_distance:
                smallest_distance = distance
                closest_pair = [previous_prime, current_prime]
        
        return closest_pair
