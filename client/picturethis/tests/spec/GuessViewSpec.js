describe( "randomLetters", function () {
    it("returns empty string", function () {
        expect(randomLetters(0)).toEqual("");
    });

    it("returns 4 random letters", function () {
        expect(randomLetters(4)).toMatch(/^[A-Z][A-Z][A-Z][A-Z]/);
    });
});

describe( "shuffleLetters", function() {
    it ("returns string of same length as input", function() {
        expect(shuffleLetters("ABCD").length).toEqual(4);
    });
});

describe( "stringDiff", function() {
    it ("returns the difference between two strings", function() {
        expect(stringDiff("dog", "antidogmatic")).toEqual("antimatic");
    });
})