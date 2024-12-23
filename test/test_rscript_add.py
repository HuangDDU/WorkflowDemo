# import pytest
# import rpy2.robjects as ro
# import rpy2.rinterface as rinterface


# # 自动的数据转换
# @ro.conversion.rpy2py.register(rinterface.IntSexpVector)
# def convert_integer(obj):
#     if len(obj) == 1:
#         return int(obj[0])
#     else:
#         return [int(x) for x in obj]


# @ro.conversion.rpy2py.register(rinterface.FloatSexpVector)
# def convert_double(obj):
#     if len(obj) == 1:
#         return float(obj[0])
#     else:
#         return [float(x) for x in obj]


# @pytest.mark.skipif(True, reason="Skip R")
# def test_rscript_add():
#     # 测试rpy2, 调用R脚本
#     r_script = """
#     add <- function(a, b) {
#         return (a+b)
#     }
#     c <- add(1,2)
#     c
#     """
#     c = ro.r(r_script)
#     # 获得输出并判断
#     assert c == 3


# if __name__ == "__main__":
#     pytest.main(["-v", __file__])
