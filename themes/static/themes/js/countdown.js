$(document).ready(function () {
    $('#clock').countdown("2020/10/10", function(event) {
        var totalHours = event.offset.totalDays * 24 + event.offset.hours;
        $(this).html(event.strftime(totalHours + ' hr %M min %S sec'));
    });
});
