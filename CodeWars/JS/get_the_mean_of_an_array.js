function getAverage(marks){
    let marksTotal = marks.length;
    let marksTotalSum = marks.reduce((x, y) => x + y);
    return Math.floor(marksTotalSum / marksTotal);
