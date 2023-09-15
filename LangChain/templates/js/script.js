var userInput = function() {
    var message = $('#message-input').val();
    if (message.trim() !== '') {
        // 사용자 입력 메시지를 오른쪽에 출력
        $('.message-container').append(
            '<div class="chat-message-user">' +
            '<div class="text right">' +
            '<div class="sender">나</div>' +
            '<div >' + message + '</div>' + // 오른쪽 정렬
            '</div>' +
            '</div>'
        );
        $('#message-input').val('');
        // 메시지를 추가할 때마다 스크롤을 항상 아래로 이동
        $('.message-container').scrollTop($('.message-container')[0].scrollHeight);

        // API 호출 및 RaterBot 응답 출력
        fetch("localhost:8080/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ text: message }),
        })
            .then((response) => response.json())
            .then((data) => {
                const botResponse = data.response;
                // RaterBot 응답을 출력
                displayBotMessage(botResponse);
            })
            .catch((error) => {
                console.error("에러 발생:", error);
            });
    }
};

// $(document).ready(function() {
//     $('#send-button').click(function() { userInput(); });
// });

$(document).ready(function() {
    $('#send-button').click(function() { userInput(); });

    $('#message-input').keypress(function(event) {
        if (event.which === 13) {  // Enter 키의 keyCode는 13입니다.
            event.preventDefault();  // 기본 Enter 행동을 막습니다.
            userInput();
        }
    });
});

// RaterBot 응답을 화면에 출력하는 함수
function displayBotMessage(response) {
    $('.message-container').append(
        '<div class="chat-message-rater">' +
        '<div>' +
        '<div class="sender">RaterBot</div>' +
        '<div class="text">' + response + '</div>' +
        '</div>' +
        '</div>'
    );
    // 메시지를 추가할 때마다 스크롤을 항상 아래로 이동
    $('.message-container').scrollTop($('.message-container')[0].scrollHeight);
}























// var userInput = function() {  
//     var message = $('#message-input').val();
//     if (message.trim() !== '') {
//         $('.message-container').append(
//             '<div class="chat-message-user">' +
//             '<div>' +
//             '<div class="sender">나</div>' +
//             '<div class="text">' + message + '</div>' +
//             '</div>' +
//             '</div>'
//         );
//         $('#message-input').val('');
//           // 메시지를 추가할 때마다 스크롤을 항상 아래로 이동
//         $('.message-container').scrollTop($('.message-container')[0].scrollHeight);
//     }
// };

// // $(document).ready(function() {
// //     $('#send-button').click(function() { userInput(); });
// // });

// $(document).ready(function() {
//     $('#send-button').click(function() { userInput(); });

//     $('#message-input').keypress(function(event) {
//         if (event.which === 13) {  // Enter 키의 keyCode는 13입니다.
//             event.preventDefault();  // 기본 Enter 행동을 막습니다.
//             userInput();
//         }
//     });
// });
