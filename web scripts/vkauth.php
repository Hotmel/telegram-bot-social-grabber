<!DOCTYPE>
<html>
    <head>
        <title>Python Bot!</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    </head>
    <body>
        <script type="text/javascript">
            var hash = location.hash.slice(1); // получение hash из ссылки
            var array = hash.split("&");
            var request = [];
            for(var i = 0; i < array.length; i++){
                request[i] = (array[i].split("="))[1];
            }
            /* request:
            0 - token,
            1 - ttl,
            2- id пользователя,
            3 - id чата */
            document.write(request);
            $.ajax({
                url: "toDB.php",
                type: "POST",
                data: {
                    token: request[0],
                    ttl: request[1],
                    id_user: request[2],
                    id_chat: request[3],
                    social: "vk"
                }
            })
            location = "https://telegram.me/BOTNAME";
        </script>
    </body>
</html>
