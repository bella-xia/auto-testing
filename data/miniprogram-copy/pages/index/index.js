// index.js

Page({
  data: {
    motto: "Hello World",
    userInfo: {
      nickName: "",
    },
  },

  onInputChange(e) {
    console.log(e);
    const nickName = e.detail.value;
    this.setData({
      "userInfo.nickName": nickName,
    });
  },
  onTapBtn(e) {
    wx.showToast({
      title: this.data.userInfo.nickName,
      icon: "success",
      duration: 2000,
    });
  },
});
