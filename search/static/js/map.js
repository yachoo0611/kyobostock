var store = seoul.concat(not_seoul);
var markers = []; // 마커를 담을 배열
var positions = new Array(); // 지점 정보를 담을 배열

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(37.535442, 126.9883856), // 지도의 중심좌표
        level: 8 // 지도의 확대 레벨
    };
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성  

for (var i = 0; i < store.length; i++){
    var p = new Object(); // positions에 담을 객체 생성
    p.title = store[i].fields.place_name;
    p.road_address_name = store[i].fields.road_address_name;
    p.phone = store[i].fields.phone;
    p.latlng = new kakao.maps.LatLng(Number(store[i].fields.y), Number(store[i].fields.x));
    p.stock = store[i].fields.stock;
    positions.push(p)
}

for (var i = 0; i < positions.length; i ++) {
    if (positions[i].stock == 0){
        continue;
    }
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
    });
}

marker.setMap(map); // 마커 지도 위에 표시

var p = JSON.stringify(positions);
document.write(p)