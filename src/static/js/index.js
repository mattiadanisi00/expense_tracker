function addExpense(amount, is_income) {
    $.post('/transaction', {amount: amount, is_income: is_income},  (data) => {
        console.log(data)
    });
}
function displayBalance(balance) {
    $('#balance .balance-amount').text(balance)
}
function displayIncomes(incomes) {
    $('#balance .profit h3').text(incomes)
}
function displayExpenses(expenses) {
    $('#balance .spend h3').text(expenses)
}
function getBalance() {
    $.post('/balance').done((data) => {
        displayBalance(data)
    })
}
function getExpenses() {
    $.post('/expenses').done((data) => {
        displayExpenses(data)
    })
}
function getIncomes() {
    $.post('/incomes').done((data) => {
        displayIncomes(data)
    })
}
function reloadUi() {
    getIncomes()
    getExpenses()
    getBalance()
}



$(function () {
    //HTML is fully loaded
    reloadUi()

    let incomesBtn = $('#incomes-btn')
    let expensesBtn = $('#expenses-btn')

    incomesBtn.on('click', () => {
        let amount = $('#amount').val();

        if (amount === '') {
            console.log('amount can not be null\n')
        } else {
            addExpense(amount, 1)
            location.reload()
        }
    })

    expensesBtn.on('click', () => {
        let amount = $('#amount').val();

        if (amount === '') {
            console.log('amount can not be null\n')
        } else {
            addExpense(amount, 0)
            location.reload()
        }
    })
})