// https://leetcode.com/problems/letter-case-permutation

// learning more about binary trees and depth-first search with this guy https://www.youtube.com/watch?v=8ncNSmLVB4E

let letterCasePermutation = function (string) {
  let result = [];
  let x = [];

  const depth_first_search = (i, string, slate) => {
    if ((i, string, slate)) {
      if (i === string.length) {
        result.push(slate.join(""));
        return;
      }
      let character = string[i];

      if (!Number.isInteger(parseInt(character))) {
        // to Uper Case
        slate.push(character.toUpperCase());
        depth_first_search(i + 1, string, slate);
        slate.pop();

        // to Lower Case
        slate.push(character.toLowerCase());
        depth_first_search(i + 1, string, slate);
        slate.pop();
      } else {
        slate.push(character);
        depth_first_search(i + 1, string, slate);
        slate.pop();
      }
    }
  };
  depth_first_search(0, string, []);
  return result;
};

// change string to test other scenarios
console.log(letterCasePermutation("a1b2"));
console.log(letterCasePermutation("3z4"));
