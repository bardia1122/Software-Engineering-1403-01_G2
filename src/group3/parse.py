def find_suggestions(inputStr, outputStr):
    # تابع کمکی برای محاسبه ماتریس LCS در سطح کلمات
    def lcs_matrix(a, b):
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp

    # تابع برای بازسازی LCS
    def traceback_lcs(dp, a, b):
        i, j = len(a), len(b)
        lcs_indices = []
        while i > 0 and j > 0:
            if a[i - 1] == b[j - 1]:
                lcs_indices.append((i - 1, j - 1))
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return lcs_indices[::-1]

    # تقسیم رشته به کلمات و ذخیره موقعیت‌های آن‌ها
    def split_with_indices(s):
        words = []
        indices = []
        current = 0
        for word in s.split():
            start = s.find(word, current)
            end = start + len(word)
            words.append(word)
            indices.append((start, end))
            current = end
        return words, indices

    input_words, input_indices = split_with_indices(inputStr)
    output_words, output_indices = split_with_indices(outputStr)

    # محاسبه ماتریس و شاخص‌های LCS
    dp = lcs_matrix(input_words, output_words)
    lcs_indices = traceback_lcs(dp, input_words, output_words)

    # شناسایی تغییرات
    suggestions = []
    input_idx = 0
    output_idx = 0
    lcs_pos = 0

    while input_idx < len(input_words) or output_idx < len(output_words):
        if (lcs_pos < len(lcs_indices) and
            input_idx < len(input_words) and
            output_idx < len(output_words) and
            input_idx == lcs_indices[lcs_pos][0] and
            output_idx == lcs_indices[lcs_pos][1]):
            # تطابق در LCS پیدا شد، حرکت به کلمه بعدی
            input_idx += 1
            output_idx += 1
            lcs_pos += 1
        else:
            # شروع تغییر
            if input_idx < len(input_words):
                start_input, end_input = input_indices[input_idx]
            else:
                start_input, end_input = len(inputStr), len(inputStr)
            if output_idx < len(output_words):
                start_output, end_output = output_indices[output_idx]
                suggest = output_words[output_idx]
                output_idx += 1
            else:
                suggest = ''
            suggestions.append({
                "start": start_input,
                "end": end_input,
                "suggest": suggest
            })
            if input_idx < len(input_words):
                input_idx += 1

    print(inputStr, " ", outputStr, " ", suggestions)
    return suggestions

input_string = 'میتوانم'
output_string = 'می‌توانم'
print(find_suggestions(input_string, output_string))
