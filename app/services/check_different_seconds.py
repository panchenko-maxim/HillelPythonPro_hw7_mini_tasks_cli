def check_different_seconds(check_seconds: int, time_for_check: int, time_now: int) -> tuple[int, bool]:
    if time_now - time_for_check > check_seconds:
        return time_now, True
    return time_for_check, False