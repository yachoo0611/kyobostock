var markers = []; // 마커를 담을 배열

var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = {
        center: new kakao.maps.LatLng(37.535442, 126.9883856), // 지도의 중심좌표
        level: 8 // 지도의 확대 레벨
    };  
  
var map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성  

var positions = [
    {
        title: '광화문', 
        latlng: new kakao.maps.LatLng(37.5709641, 126.9755758)
    },
    {
        title: '가든파이브', 
        latlng: new kakao.maps.LatLng(37.4772225, 127.1225181)
    },
    {
        title: '강남', 
        latlng: new kakao.maps.LatLng(37.5037059, 127.0219459)
    },
    {
        title: '동대문',
        latlng: new kakao.maps.LatLng(37.5682965, 127.0055087)
    }
];    

for (var i = 0; i < positions.length; i ++) {
    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
    });
}

marker.setMap(map); // 마커 지도 위에 표시

// 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// marker.setMap(null);    