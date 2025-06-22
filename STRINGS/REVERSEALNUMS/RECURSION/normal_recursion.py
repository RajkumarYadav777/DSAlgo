def reverse_alnum_only_normal(s):
    def collect_alnums(i):
        if i == len(s):
            return []
        if s[i].isalnum():
            return [s[i]] + collect_alnums(i + 1)
        else:
            return collect_alnums(i + 1)

    def build_result(i, alnums):
        if i == len(s):
            return ''
        if s[i].isalnum():
            return alnums.pop() + build_result(i + 1, alnums)
        else:
            return s[i] + build_result(i + 1, alnums)

    alnum_chars = collect_alnums(0)  # Collect in forward
    return build_result(0, alnum_chars)  # Rebuild in reverse
