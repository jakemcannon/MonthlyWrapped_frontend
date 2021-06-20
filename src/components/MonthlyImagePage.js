import React from 'react'
import ImageGrid from './ImageGrid';

import MonthlyImage from './MonthlyImage'

var today = new Date();
var lastDayOfMonth = new Date(today.getFullYear(), today.getMonth()+1, 0);

var tomorrow = new Date();
console.log(today.getTime())
console.log(tomorrow.getTime())
console.log(lastDayOfMonth.getTime())

if (today != lastDayOfMonth) {
    console.log("It is not the last day of the month")
}

if (today == tomorrow) {
    console.log("It is the last day of the month")
}
console.log(today.getTime() == tomorrow.getTime())
console.log(today)
console.log(tomorrow)

function MonthlyImagePage() {

    if (today.getTime() != lastDayOfMonth.getTime()) {
        return <MonthlyImage />
    }

    return "Not the end of the month yet"
}

export default MonthlyImagePage
