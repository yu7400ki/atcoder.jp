def minimum_window_width(N, M, word_widths):
    min_width = 1
    max_width = sum(word_widths) + (N - 1)

    while min_width <= max_width:
        mid_width = (min_width + max_width) // 2
        lines_required = 1
        current_line_width = 0

        for width in word_widths:
            if current_line_width + width <= mid_width:
                current_line_width += width + 1  # Add a space
            else:
                lines_required += 1
                current_line_width = width

        if lines_required <= M:
            max_width = mid_width - 1
        else:
            min_width = mid_width + 1

    return min_width

# Example usage:
N, M = map(int, input().split())
L = list(map(int, input().split()))
result = minimum_window_width(N, M, L)
print(result)  # Output: 5
