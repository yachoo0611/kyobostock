var store = seoul.concat(not_seoul);
var markers = []; // 마커를 담을 배열
var positions = new Array(); // 지점 정보를 담을 배열

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(37.535442, 126.9883856), // 지도의 중심좌표
        level: 8 // 지도 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성  

// positions에 각 지점 정보 입력위한 for문
for (var i = 0; i < store.length; i++){
    var p = new Object(); // positions에 담을 객체 생성
    // fields는 각 지점의 실질적인 정보를 담고있는 dict
    p.title = store[i].fields.place_name;
    p.road_address_name = store[i].fields.road_address_name;
    p.phone = store[i].fields.phone;
    p.latlng = new kakao.maps.LatLng(Number(store[i].fields.y), Number(store[i].fields.x));
    p.stock = store[i].fields.stock;
    p.pk = store[i].pk;
    positions.push(p);
}

for (var i = 0; i < positions.length; i ++) {
    if (positions[i].stock == 0){
        continue;
    }
    // 마커 생성
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title: positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
    });
    
    // marker.setMap(map); // 마커 지도 위에 표시
    
    // 인포윈도우에 입력할 content
    var iwcontent = '<div class="iw_wrap">' + 
        '<div class="iw_title">' + positions[i].title + '</div>' +
        '<div>' + positions[i].stock + '</div>' +
        '<div>' + positions[i].phone + '</div>' +
        '<div class="desc address">' + positions[i].road_address_name + '</div>' +
        '</div>'
    // 마커에 표시할 인포윈도우 생성
    var infowindow = new kakao.maps.InfoWindow({
        removable: true,
        content: iwcontent
    });

    (function(marker, infowindow) {
        // 마커에 click 이벤트 등록
        kakao.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map, marker);
        });
    })(marker, infowindow);
}

// 지점명 클릭 시 해당 마커로 지도 이동
$(".stock_table").on("click", "th", function() {
    var place = $(this).text(); // 지점명
    var mv = new Object; // 좌표(객체) 받기 위한 변수
    // 클릭한 지점명과 동일한 positions 배열의 좌표를 받아옴
    $.each(positions, function(index, item) {
        if (item.title == place){
            mv = item.latlng;
            return;
        }
    });
    panTo(mv);
});    

function panTo(mv) {
    // 이동할 위도 경도 위치 생성
    var moveLatLon = mv;
    // 지도 중심 이동
    map.panTo(moveLatLon);
}
