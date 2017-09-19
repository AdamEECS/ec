const data = [
    {
        room: '走廊',
        css: {
            width: 235,
            height: 90,
        },
        edge: '走廊建筑面积',
        edgeCss: {
            width: 235,
            height: 100,
            bottom: 630,
            right: 250,
        },
        items: [
            {
                id: '扫地机',
                data: {
                    价格: 3299,
                    品牌: 'iRobot 891',
                    链接: "https://item.jd.com/5014090.html?",
                },
                css: {
                    width: 36,
                    height: 36,
                    top: 0,
                    left: 10,
                    outline: 'none',
                    border: '1px solid black',
                    'border-radius': '50%',
                },
            },
        ],
    },
    {
        room: '次卧',
        css: {
            width: 233,
            height: 340,
        },
        edge: '次卧建筑面积',
        edgeCss: {
            width: 250,
            height: 380,
            top: 0,
            right: 0,
        },
        door: '次卧门',
        doorCss: {
            width: 20,
            height: 100,
            'writing-mode': 'vertical-lr',
            'background-color': 'white',
            position: 'absolute',
            bottom: 0,
            left: -12,
        },
        items: [
            {
                id: '次卧床',
                data: {
                    价格: 2999,
                    品牌: '宜家 马尔姆',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/60274921",
                },
                css: {
                    width: 209,
                    height: 166,
                    top: 0,
                    right: 0,
                },
            },
            {
                id: '次卧床垫',
                data: {
                    价格: 1499,
                    品牌: '宜家 海沃格',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/10269352/",
                },
                css: {
                    width: 100,
                    height: 100,
                    top: 40,
                    right: 10,
                },
            },{
                id: '储物袋*8',
                data: {
                    价格: 320,
                    品牌: '宜家 思库布',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/70294990/",
                },
                css: {
                    width: 69,
                    height: 55,
                    top: 40,
                    right: 120,
                },
            },
            {
                id: '工作桌',
                data: {
                    价格: 649,
                    品牌: '宜家 希勒',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/S89047155/",
                },
                css: {
                    width: 65,
                    height: 140,
                    top: 170,
                    right: 0,
                },
            },{
                id: '屏幕支架*2',
                data: {
                    价格: 818,
                    品牌: '乐歌 D8A',
                    链接: "https://item.jd.com/4163789.html",
                },
                css: {
                    width: 20,
                    height: 110,
                    top: 190,
                    right: 0,
                },
            },
            {
                id: '工作椅1',
                data: {
                    价格: 2358,
                    品牌: '金豪',
                    链接: "https://item.jd.com/4486479.html",
                },
                css: {
                    width: 66,
                    height: 55,
                    top: 180,
                    right: 70,
                },
            },
            {
                id: '工作椅2',
                data: {
                    价格: 2650,
                    品牌: 'Marrit',
                    链接: "https://item.jd.com/1298733706.html",
                },
                css: {
                    width: 66,
                    height: 55,
                    top: 250,
                    right: 70,
                },
            },
            {
                id: '次卧空调',
                data: {
                    价格: 3048,
                    品牌: '松下 1匹',
                    链接: "https://item.jd.com/1451088.html",
                },
                css: {
                    width: 24,
                    height: 78,
                    bottom: 170,
                    right: 1,
                    'writing-mode': 'vertical-lr',
                },
            },
        ],
    },
    {
        room: '洗手间',
        css: {
            width: 220,
            height: 250,
            "clip-path": "polygon( 43px 110px, 125px 110px, 125px 0px, 235px 0px, 235px 250px, 43px 250px)",
            top: '50%',
            left: '50%',
            position: 'absolute',
            transform: "translate(-50%, -50%)",
            'text-align': 'right',
        },
        edge: '洗手间建筑面积',
        edgeCss: {
            width: 235,
            height: 280,
            top: 0,
            right: 250,
            'clip-path': "polygon( 0px 110px, 125px 110px, 125px 0px, 235px 0px, 235px 280px, 0px 280px)",
        },
        door: '洗手间门',
        doorCss: {
            width: 100,
            height: 20,
            'background-color': 'white',
            position: 'absolute',
            bottom: -2,
            left: 50,
        },
        items: [
            {
                id: '淋浴间',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 100,
                    height: 110,
                    top: 0,
                    right: 0,
                },
            },
            {
                id: '马桶',
                data: {
                    价格: 0,
                    品牌: 'TOTO',
                },
                css: {
                    width: 40,
                    height: 60,
                    bottom: 80,
                    right: 120,
                },
            },
            {
                id: '洗脸池',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 40,
                    height: 100,
                    bottom: 0,
                    right: 0,
                },
            },
        ],
    },
    {
        room: '客厅及餐厅',
        css: {
            width: 321,
            height: 610,
        },
        edge: '客厅及餐厅建筑面积',
        edgeCss: {
            width: 350,
            height: 630,
            bottom: 0,
        },
        items: [
            {
                id: '餐厅壁柜',
                data: {
                    价格: 800,
                    品牌: '宜家 伊克特',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/90333957",
                },
                css: {
                    width: 140,
                    height: 35,
                    top: 0,
                    left: 0,
                    'z-index': 10,
                },
            },
            {
                id: '餐桌',
                data: {
                    价格: 999,
                    品牌: '宜家 利萨伯',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/80365717/",
                },
                css: {
                    width: 140,
                    height: 78,
                    top: 80,
                    left: 0,
                    'z-index': 10,
                },
            },
            {
                id: '餐椅1',
                data: {
                    价格: 499,
                    品牌: '宜家',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/40359997/",
                },
                css: {
                    top: 40,
                    left: 10,
                    width: 50,
                    height: 50,
                },
            },
            {
                id: '餐椅2',
                data: {
                    价格: 499,
                    品牌: '宜家',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/40359997/",
                },
                css: {
                    top: 40,
                    left: 80,
                    width: 50,
                    height: 50,
                },
            },
            {
                id: '餐椅3',
                data: {
                    价格: 499,
                    品牌: '宜家',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/40359997/",
                },
                css: {
                    top: 155,
                    left: 10,
                    width: 50,
                    height: 50,
                },
            },
            {
                id: '餐椅4',
                data: {
                    价格: 499,
                    品牌: '宜家',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/40359997/",
                },
                css: {
                    top: 155,
                    left: 80,
                    width: 50,
                    height: 50,
                },
            },
            {
                id: '镜子',
                data: {
                    价格: 699,
                    品牌: '宜家 霍维特',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/60178892/",
                },
                css: {
                    width: 10,
                    height: 78,
                    top: 110,
                    right: 2,
                },
            },
            {
                id: '一人沙发',
                data: {
                    价格: 4299,
                    品牌: 'Lazboy',
                    链接: "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16356361476.102.46f16db0Q6IKj2&id=549480019747&rn=c380ff7ed9417daf3e16df3b65b53032&abbucket=10&skuId=3584624935732",
                },
                css: {
                    width: 104,
                    height: 105,
                    bottom: 250,
                    left: 50,
                    'z-index': 10,
                    transform: 'rotate(30deg)',
                },
            },
            {
                id: '三人沙发',
                data: {
                    价格: 8499,
                    品牌: 'Lazboy',
                    链接: "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-16356361476.102.46f16db0Q6IKj2&id=549480019747&rn=c380ff7ed9417daf3e16df3b65b53032&abbucket=10&skuId=3584624935730",
                },
                css: {
                    width: 104,
                    height: 217,
                    bottom: 10,
                    left: 20,
                    'z-index': 10,
                },
            },
            {
                id: '立柜',
                data: {
                    价格: 389,
                    品牌: '宜家 毕利',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/S19217735/",
                },
                css: {
                    width: 28,
                    height: 40,
                    bottom: 242,
                    left: 0,
                    'z-index': 10,
                },
            },
            {
                id: '墙搁板',
                data: {
                    价格: 488,
                    品牌: '宜家 埃克比 莫斯比 / 埃克比 比亚姆',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/S69885470/",
                },
                css: {
                    width: 28,
                    height: 239,
                    bottom: 0,
                    left: 0,
                    'z-index': 10,
                },
            },
            {
                id: '茶几1',
                data: {
                    价格: 249,
                    品牌: '宜家 新贝',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/60295928/#/60295928",
                },
                css: {
                    width: 50,
                    height: 50,
                    bottom: 170,
                    left: 150,
                    'z-index': 10,
                },
            },
            {
                id: '茶几2',
                data: {
                    价格: 249,
                    品牌: '宜家 新贝',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/60295928/#/60295928",
                },
                css: {
                    width: 50,
                    height: 50,
                    bottom: 80,
                    left: 150,
                    'z-index': 10,
                },
            },
            {
                id: '投影墙',
                data: {
                    价格: 4599,
                    品牌: '极米 H1S',
                    链接: "https://item.jd.com/4860246.html",
                },
                css: {
                    width: 10,
                    height: 240,
                    bottom: 20,
                    right: 2,
                },
            },
            {
                id: '地毯',
                data: {
                    价格: 599,
                    品牌: '宜家 阿达姆',
                    链接: "//www.ikea.com/cn/zh/catalog/products/30174616/#/70174619",
                },
                css: {
                    width: 170,
                    height: 240,
                    bottom: 30,
                    left: 100,
                    'z-index': 1,
                    'text-align': 'right',
                },
            },
            {
                id: '客厅空调',
                data: {
                    价格: 3348,
                    品牌: '松下 1.5匹',
                    链接: "https://item.jd.com/1451093.html",
                },
                css: {
                    width: 24,
                    height: 78,
                    bottom: 5,
                    left: 1,
                    'writing-mode': 'vertical-lr',
                    'z-index': 20,
                },
            },
        ],
    },
    {
        room: '玄关',
        css: {
            width: 150,
            height: 240,
        },
        edge: '玄关建筑面积',
        edgeCss: {
            width: 170,
            height: 250,
            bottom: 630,
            left: 215,
        },
        door: '正门',
        doorCss: {
            width: 100,
            height: 20,
            top: -15,
            left: 10,
            'background-color': 'white',
            position: 'absolute',
        },
        items: [
            {
                id: '衣帽鞋柜',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 40,
                    height: 80,
                    top: 0,
                    right: 0,
                },
            },
            {
                id: '玄关到客厅',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 110,
                    height: 20,
                    bottom: -20,
                    'background-color': 'white',
                    position: 'absolute',
                    outline: 'none',
                },
            },
            {
                id: '玄关到走廊',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 20,
                    height: 90,
                    bottom: 0,
                    right: -12,
                    'writing-mode': 'vertical-lr',
                    'background-color': 'white',
                    position: 'absolute',
                    outline: 'none',
                },
            },
        ],
    },
    {
        room: '洗衣间',
        css: {
            width: 80,
            height: 57,
        },
        edge: '洗衣间建筑面积',
        edgeCss: {
            width: 100,
            height: 70,
            bottom: 730,
            left: 335,
        },
        items: [
            {
                id: '洗衣机',
                data: {
                    价格: 7199,
                    品牌: '海尔 EG8014HB88LGU1',
                    特性: '8公斤直驱变频洗烘一体',
                    链接: "https://item.jd.com/3655643.html",
                },
                css: {
                    width: 62,
                    height: 48,
                    top: 5,
                    left: 10,
                },
            },
        ],
    },
    {
        room: '厨房',
        css: {
            width: 310,
            height: 200,
        },
        edge: '厨房建筑面积',
        edgeCss: {
            width: 330,
            height: 220,
            bottom: 410,
            left: 350,
        },
        door: '厨房门',
        doorCss: {
            width: 20,
            height: 100,
            top: 10,
            left: -12,
            'writing-mode': 'vertical-lr',
            'background-color': 'white',
            position: 'absolute',
        },
        items: [
            {
                id: '冰箱',
                data: {
                    价格: 2999,
                    品牌: '海尔 BCD-325WDSD',
                    链接: "https://item.jd.com/1792767.html",
                },
                css: {
                    width: 64,
                    height: 68,
                    bottom: 3,
                    left: 5,
                },
            },{
                id: '洗碗机',
                data: {
                    价格: 3580,
                    品牌: '松下 台式',
                    链接: "https://item.jd.com/3073802.html",
                },
                css: {
                    width: 35,
                    height: 55,
                    bottom: 3,
                    right: 5,
                    'writing-mode': 'vertical-lr',
                    'z-index': 10,
                },
            },
            {
                id: '操作台',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 235,
                    height: 61,
                    bottom: 0,
                    right: 0,
                },
            },

        ],
    },
    {
        room: '主卧',
        css: {
            width: 301,
            height: 396,
        },
        edge: '主卧建筑面积',
        edgeCss: {
            width: 330,
            height: 410,
            bottom: 0,
            left: 350,
        },
        door: '主卧门',
        doorCss: {
            width: 20,
            height: 100,
            top: 10,
            left: -12,
            'writing-mode': 'vertical-lr',
            'background-color': 'white',
            position: 'absolute',
        },
        items: [
            {
                id: '主卧柜子',
                data: {
                    价格: 0,
                    品牌: '万科',
                },
                css: {
                    width: 205,
                    height: 60,
                    top: 0,
                    right: 0,
                },
            },
            {
                id: '主卧床',
                data: {
                    价格: 5000,
                    品牌: '舒达',
                    链接: "http://www.serta.cn/product_show/show-450.html",
                },
                css: {
                    width: 210,
                    height: 185,
                    top: 120,
                    right: 0,
                },
            },
            {
                id: '主卧床垫',
                data: {
                    价格: 30200,
                    品牌: '丝涟',
                    链接: "https://detail.tmall.com/item.htm?spm=a1z10.3-b-s.w4011-15139193946.60.46f16db03e8WHi&id=45336990917&rn=0ae58f7c2e46abd7efc7940d3132f4c3&abbucket=10&skuId=3239595849974",
                },
                css: {
                    width: 200,
                    height: 155,
                    top: 140,
                    right: 10,
                },
            },
            {
                id: '化妆台',
                data: {
                    价格: 599,
                    品牌: '宜家 百灵',
                    链接: "http://www.ikea.com/cn/zh/catalog/products/90355421/",
                },
                css: {
                    width: 42,
                    height: 70,
                    bottom: 10,
                    right: 0,
                    'writing-mode': 'vertical-lr',
                },
            },
            {
                id: '化妆镜',
                data: {
                    价格: 1000,
                    品牌: '预留位',
                },
                css: {
                    width: 20,
                    height: 50,
                    bottom: 20,
                    right: 2,
                    'writing-mode': 'vertical-lr',
                },
            },
            {
                id: '主卧空调',
                data: {
                    价格: 3048,
                    品牌: '松下 1匹',
                    链接: "https://item.jd.com/1451088.html",
                },
                css: {
                    width: 24,
                    height: 78,
                    bottom: 5,
                    left: 1,
                    'writing-mode': 'vertical-lr',
                },
            },
        ],
    },
    {
        room: '庭院',
        css: {
            width: '100%',
            height: '100%',
        },
        edge: '庭院建筑面积',
        edgeCss: {
            width: 190,
            height: 630,
            bottom: 0,
            right: 0,
        },
        items: [
            {
                id: '窗外庭院',
                data: {
                    价格: 0,
                },
                css: {
                    width: '100%',
                    height: '100%',
                    'background-color': 'lightblue',
                },
            },
        ],
    },
]
