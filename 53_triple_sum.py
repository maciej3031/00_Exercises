# Note: Write a solution with O(n2) time complexity
#
# You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three
#  elements for which the sum is exactly x.

# Example:
#
# For x = 15 and a = [14, 1, 2, 3, 8, 15, 3], the output should be
# tripletSum(x, a) = false;
#
# For x = 8 and a = [1, 1, 2, 5, 3], the output should be
# tripletSum(x, a) = true.
#
# The given array contains the elements 1,2, and 5, which add up to 8.
#
from itertools import combinations


def tripletSum(x, a):
    for i in combinations(a, 3):
        if sum(i) == x:
            return True
    return False

print(tripletSum(15, [14, 1, 2, 3, 8, 15, 3]))
print(tripletSum(1291, [162, 637, 356, 768, 656, 575, 32, 53, 351, 151, 942, 725, 967, 431, 108, 192, 8, 338, 458, 288,
                        754, 384, 946, 910, 210, 759, 222, 589, 423, 947, 507, 31, 414, 169, 901, 592, 763, 656, 411,
                        360, 625, 538, 549, 484, 596, 42, 603, 351, 292, 837, 375, 21, 597, 22, 349, 200, 669, 485,
                        282, 735, 54, 1000, 419, 939, 901, 789, 128, 468, 729, 894, 649, 484, 808, 422, 311, 618, 814,
                        515, 310, 617, 936, 452, 601, 250, 520, 557, 799, 304, 225, 9, 845, 610, 990, 703, 196, 486,
                        94, 344, 524, 588, 315, 504, 449, 201, 459, 619, 581, 797, 799, 282, 590, 799, 10, 158, 473,
                        623, 539, 293, 39, 180, 191, 658, 959, 192, 816, 889, 157, 512, 203, 635, 273, 56, 329, 647,
                        363, 887, 876, 434, 870, 143, 845, 417, 882, 999, 323, 652, 22, 700, 558, 477, 893, 390, 76,
                        713, 601, 511, 4, 870, 862, 689, 402, 790, 256, 424, 3, 586, 183, 286, 89, 427, 618, 758, 833,
                        933, 170, 155, 722, 190, 977, 330, 369, 693, 426, 556, 435, 550, 442]))

