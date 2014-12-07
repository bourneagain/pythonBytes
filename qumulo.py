__author__ = 'shyam'

"""
We are looking for correct, clean and maintainable code (production quality code).
Please keep it short and avoid duplication of code. Although the code given to you is C/C++, feel free to use any
programming language.

Please use simple linear search (not binary search).
Please implement the given function and include functional tests to verify correctness of the implementation.

enum SearchType {
    LESS_THAN,
    LESS_THAN_OR_EQUAL,
    EQUAL,
    GREATER_THAN_OR_EQUAL,
    GREATER_THAN,
};

enum SearchResult {
    NOT_FOUND,
    FOUND_EXACT,
    FOUND_GREATER,
    FOUND_LESS,
};

/*
 * Search an array of sorted numbers.
 *
 * items    : An array of sorted ints, with no duplicates
 * n_items  : The size of the items array
 * ascending: true if and only if the array is sorted in ascending order
 * key      : the key to search for
 * type     : the type of match to find
 *
 * This function finds the element in the array
 * that best fits the search criteria. It returns
 * the match type and the index of the matching item.
 *
 * LESS_THAN
 * ---------
 *  Finds the largest item which is less than the key.
 *  It returns FOUND_LESS if a match is found, NOT_FOUND
 *  if no match is found.
 *
 * LESS_THAN_OR_EQUAL
 * ------------------
 *  Finds the item which is equal to the key, or the
 *  largest item which is less than the key. Returns
 *  FOUND_EXACT if an item that exactly matches the key
 *  is found, FOUND_LESS If a non-exact match is found
 *  and NOT_FOUND if no match is found.
 *
 * EQUAL
 * -----
 *  Finds an item which is equal to the key. Returns
 *  FOUND_EXACT if an item if found, NOT_FOUND otherwise.
 *
 * GREATER_THAN_OR_EQUAL
 * ---------------------
 *  Finds the item which is equal to the key, or the
 *  smallest item which is greater than the key. Returns
 *  FOUND_EXACT if an item that exactly matches the key
 *  is found, FOUND_GREATER if a non-exact match is found
 *  and NOT_FOUND if no match is found.
 *
 * GREATER_THAN
 * -------------
 *  Finds the smallest item which is greater than the
 *  key. Returns FOUND_GREATER if a match if found, NOT_FOUND
 *  if no match is found.
 *
 * Examples
 * --------
 *  Given the input array [0, 2, 4, 6, 8] (ascending order)
 *
 *  +-----+-----------------------+---------------+-------+
 *  | Key | Type                  | Returns       | Index |
 *  +-----+-----------------------+---------------+-------+
 *  | -1  | LESS_THAN_OR_EQUAL    | NOT_FOUND     | X     |
 *  +-----+-----------------------+---------------+-------+
 *  |  0  | LESS_THAN             | NOT_FOUND     | X     |
 *  +-----+-----------------------+---------------+-------+
 *  |  0  | EQUAL                 | FOUND_EXACT   | 0     |
 *  +-----+-----------------------+---------------+-------+
 *  |  1  | EQUAL                 | NOT_FOUND     | X     |
 *  +-----+-----------------------+---------------+-------+
 *  |  2  | GREATER_THAN_OR_EQUAL | FOUND_EXACT   | 1     |
 *  +-----+-----------------------+---------------+-------+
 *  |  2  | GREATER_THAN          | FOUND_GREATER | 2     |
 *  +-----+-----------------------+---------------+-------+
 *
 *  Given the input array [8, 6, 4, 2, 0] (descending order)
 *
 *  +-----+-----------------------+---------------+-------+
 *  | Key | Type                  | Returns       | Index |
 *  +-----+-----------------------+---------------+-------+
 *  | -1  | LESS_THAN             | NOT_FOUND     | X     |
 *  +-----+-----------------------+---------------+-------+
 *  |  4  | LESS_THAN_OR_EQUAL    | FOUND_EXACT   | 2     |
 *  +-----+-----------------------+---------------+-------+
 *  |  8  | EQUAL                 | FOUND_EXACT   | 0     |
 *  +-----+-----------------------+---------------+-------+
 *  |  5  | GREATER_THAN_OR_EQUAL | FOUND_GREATER | 1     |
 *  +-----+-----------------------+---------------+-------+
 *  |  2  | GREATER_THAN_OR_EQUAL | FOUND_EXACT   | 3     |
 *  +-----+-----------------------+---------------+-------+
 *  |  9  | GREATER_THAN          | NOT_FOUND     | X     |
 *  +-----+-----------------------+---------------+-------+
 *
 * Assumptions
 * -----------
 *  The items are sorted
 *  Items will be non-NULL
 *  There are no duplicate items
 */
enum SearchResult
search(
    const int items[],
    unsigned n_items,
    bool ascending,
    int key,
    enum SearchType type,
    unsigned *index)
{
    return NOT_FOUND;
}

 * items    : An array of sorted ints, with no duplicates
 * n_items  : The size of the items array
 * ascending: true if and only if the array is sorted in ascending order
 * key      : the key to search for
 * type     : the type of match to find

"""

def SearchResult(items,n_items,ascending,key,SearchType,indexValue):
    # check for number
    global index
    index=indexValue
    if len(items) != n_items:
        raise Exception("I know python!")


    #for searchKey in items:

items=[8, 6, 4, 2, 0]

SearchResult(items,4,True,8,EQUAL,index)


