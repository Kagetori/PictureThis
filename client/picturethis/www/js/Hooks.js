// This file defines hooks that is called by ServerCaller

function hooks(obj) {

    // Hook for Bank
    if (obj.hasOwnProperty('bank_account')) {
        var bank_account = obj.bank_account;
        setBankInfo(bank_account);
    }
}
