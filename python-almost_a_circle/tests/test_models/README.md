# Python - Almost a circle - Testing files

The following list of tests was __unlocked after__ the deadline of the project in order to check and verify which of them were missing and improve the coerage in future tasks.

To review the complete list of main files used by the checker, take a look at: [checker_tests](./checker_tests/)

## List of all tests required for task 0:

* README.md exists and is not empty

0. Test of Base() for assigning automatically an ID exists
1. Test of Base() for assigning automatically an ID + 1 of the previous exists
2. Test of Base(89) saving the ID passed exists
3. Test of Base.to_json_string(None) exists
4. Test of Base.to_json_string([]) exists
5. Test of Base.to_json_string([ { 'id': 12 }]) exists
6. Test of Base.to_json_string([ { 'id': 12 }]) returning a string exists
7. Test of Base.from_json_string(None) exists
8. Test of Base.from_json_string("[]") exists
9. Test of Base.from_json_string('[{ "id": 89 }]') exists
10. Test of Base.from_json_string('[{ "id": 89 }]') returning a list exists
11. Test of Rectangle(1, 2) exists
12. Test of Rectangle(1, 2, 3) exists
13. Test of Rectangle(1, 2, 3, 4) exists
14. Test of Rectangle("1", 2) exists
15. Test of Rectangle(1, "2") exists
16. Test of Rectangle(1, 2, "3") exists
17. Test of Rectangle(1, 2, 3, "4") exists
18. Test of Rectangle(1, 2, 3, 4, 5) exists
19. Test of Rectangle(-1, 2) exists
20. Test of Rectangle(1, -2) exists
21. Test of Rectangle(0, 2) exists
22. Test of Rectangle(1, 0) exists
23. Test of Rectangle(1, 2, -3) exists
24. Test of Rectangle(1, 2, 3, -4) exists
25. Test of area() exists
26. Test of __str__() for Rectangle exists
27. Test of display() without x and y exists
28. Test of display() without y exists
29. Test of display() exists
30. Test of to_dictionary() in Rectangle exists
31. Test of update() in Rectangle exists
32. Test of update(89) in Rectangle exists
33. Test of update(89, 1) in Rectangle exists
34. Test of update(89, 1, 2) in Rectangle exists
35. Test of update(89, 1, 2, 3) in Rectangle exists
36. Test of update(89, 1, 2, 3, 4) in Rectangle exists
37. Test of update(**{ 'id': 89 }) in Rectangle exists
38. Test of update(**{ 'id': 89, 'width': 1 }) in Rectangle exists
39. Test of update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists
40. Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists
41. Test of update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists
42. Test of Rectangle.create(**{ 'id': 89 }) in Rectangle exists
43. Test of Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle exists
44. Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle exists
45. Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 }) in Rectangle exists
46. Test of Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 }) in Rectangle exists
47. Test of Rectangle.save_to_file(None) in Rectangle exists
48. Test of Rectangle.save_to_file([]) in Rectangle exists
49. Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists
50. Test of Rectangle.load_from_file() when file doesn’t exist exists
51. Test of Rectangle.load_from_file() when file exists exists
52. Test of Square(1) exists
53. Test of Square(1, 2) exists
54. Test of Square(1, 2, 3) exists
55. Test of Square("1") exists
56. Test of Square(1, "2") exists
57. Test of Square(1, 2, "3") exists
58. Test of Square(1, 2, 3, 4) exists
59. Test of Square(-1) exists
60. Test of Square(1, -2) exists
61. Test of Square(1, 2, -3) exists
62. Test of Square(0) exists
63. Test of __str__() for Square exists
64. Test of to_dictionary() in Square exists
65. Test of update() in Square exists
66. Test of update(89) in Square exists
67. Test of update(89, 1) in Square exists
68. Test of update(89, 1, 2) in Square exists
69. Test of update(89, 1, 2, 3) in Square exists
70. Test of update(**{ 'id': 89 }) in Square exists
71. Test of update(**{ 'id': 89, 'size': 1 }) in Square exists
72. Test of update(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists
73. Test of update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists
74. Test of Square.create(**{ 'id': 89 }) in Square exists
75. Test of Square.create(**{ 'id': 89, 'size': 1 }) in Square exists
76. Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square exists
77. Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square exists
78. Test of Square.save_to_file(None) in Square exists
79. Test of Square.save_to_file([]) in Square exists
80. Test of Square.save_to_file([Square(1)]) in Square exists
81. Test of Square.load_from_file() when file doesn’t exist exists
82. Test of Square.load_from_file() when file exists exists

### Tests not covered in my repository:

Directory: [test/test_models](../test_models/)

- 14. Test of Rectangle("1", 2) exists
- 15. Test of Rectangle(1, "2") exists
- 16. Test of Rectangle(1, 2, "3") exists
- 17. Test of Rectangle(1, 2, 3, "4") exists
- 19. Test of Rectangle(-1, 2) exists
- 20. Test of Rectangle(1, -2) exists
- 21. Test of Rectangle(0, 2) exists
- 22. Test of Rectangle(1, 0) exists
- 47. Test of Rectangle.save_to_file(None) in Rectangle exists
- 48. Test of Rectangle.save_to_file([]) in Rectangle exists
- 49. Test of Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle exists
- 55. Test of Square("1") exists
- 56. Test of Square(1, "2") exists
- 57. Test of Square(1, 2, "3") exists
- 59. Test of Square(-1) exists
- 60. Test of Square(1, -2) exists
- 62. Test of Square(0) exists 
- 78. Test of Square.save_to_file(None) in Square exists
- 79. Test of Square.save_to_file([]) in Square exists
- 80. Test of Square.save_to_file([Square(1)]) in Square exists