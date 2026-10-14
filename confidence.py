def is_confident(results, threshold=0.6):
    if not results:
        return False
    if results[0]["score"]>=threshold:
        return True
    return False    
    
    
if __name__ == "__main__":
    good = [{"score": 0.72}, {"score": 0.61}]
    weak = [{"score": 0.44}, {"score": 0.41}]
    mixed = [{"score": 0.91}, {"score": 0.41}]

    print(is_confident(good))    # expect True
    print(is_confident(weak))    # expect False
    print(is_confident(mixed))
    print(is_confident([]))      # expect False — and no crash    