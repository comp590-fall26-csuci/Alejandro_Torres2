#include "utest.h"
#include "fibonacci.h"

UTEST(Fibonacci, Terms1To10) {
    int expected[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

    for (int term = 1; term <= 10; term++) {
        ASSERT_EQ(expected[term - 1], fibonacci(term));
    }
}

UTEST(GoldenRatio, Terms1To10) {
    double expected = 1.618034;

    for (int term = 1; term <= 10; term++) {
        ASSERT_NEAR(expected, golden_ratio_approx(term), 0.000001);
    }
}

UTEST_MAIN()
