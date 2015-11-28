describe( "randomLetters", function () {
    it("produce empty string", function () {
        expect(randomLetters(0)).toEqual("");
    });

    it("produce 4 random letters", function () {
        expect(randomLetters(4)).toMatch(/^[A-Z][A-Z][A-Z][A-Z]/);
    });
});