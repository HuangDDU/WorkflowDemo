import pytest
import rpy2.robjects as ro


@pytest.mark.skipif(True)
def test_r_library():
    # 测试rpy2, 调用R的library，查看库是否安装成功
    r_script = """
    library(dynwrap)
    """
    ro.r(r_script)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
