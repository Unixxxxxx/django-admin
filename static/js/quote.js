$(document).ready(function () {
  $("#quoteForm").on("submit", function (e) {
    e.preventDefault();
    $.ajax({
      url: "/travel/get-quote/",  // Or {% url 'get_quote' %} if inside template
      method: "POST",
      data: $(this).serialize(),
      success: function (response) {
        if (response.success) {
          $("#formMsg").html("<p class='text-success'>" + response.message + "</p>");
          $("#quoteForm")[0].reset();
        } else {
          $("#formMsg").html("<p class='text-danger'>Please fix errors.</p>");
        }
      }
    });
  });
});

