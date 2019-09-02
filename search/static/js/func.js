// data = 지점 정보, table = 자료를 입력할 테이블
var drawTable = function (data, table) {
    t = 0; // 지점 수를 체크하기 위한 변수
    // 8개 열이 들어가는 행 생성을 위한 for문
    for(i=0; i<(data.length/8); i++){
        var row1= $("<tr />"); // 지점명 행(th)
        var row2= $("<tr />"); // 재고 행(td)
        $(table).append(row1);
        $(table).append(row2);
        // 8개 열에 각 지점, 재고 정보 입력 위한 for문
        for(j=0; j<8; j++){
            // t가 지점 수 보다 클 경우 for문 종료
            if (t > (data.length-1)) break;
            row1.append($("<th>" + data[t].info.place + "</th>"));
            row2.append($("<td>" + data[t].info.s + "</td>"));
            t++;
        }
    }
}
