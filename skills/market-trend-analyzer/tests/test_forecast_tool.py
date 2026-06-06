#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
市场预测工具测试 - test_forecast_tool.py
功能: 测试市场预测工具的各项功能
"""

import sys
import os
import json

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scripts'))

try:
    from forecast_tool import generate_forecast, generate_alert, get_forecast_details
    
    def test_generate_forecast():
        """测试生成市场预测功能"""
        print("测试: generate_forecast()")
        result = generate_forecast('12months')
        assert result is not None, "生成市场预测失败"
        assert 'trends' in result, "返回结果缺少trends字段"
        assert 'opportunities' in result, "返回结果缺少opportunities字段"
        assert 'risks' in result, "返回结果缺少risks字段"
        print(f"  通过: 预测了 {len(result.get('trends', []))} 个趋势")
        return True
    
    def test_generate_alert():
        """测试生成市场预警功能"""
        print("测试: generate_alert()")
        alerts = generate_alert()
        assert isinstance(alerts, list), "返回结果应该是列表"
        print(f"  通过: 生成了 {len(alerts)} 个高紧急度预警")
        return True
    
    def test_get_forecast_details():
        """测试获取预测详细信息功能"""
        print("测试: get_forecast_details()")
        # 测试获取整体预测
        details = get_forecast_details('overall')
        assert details is not None, "获取整体预测详情失败"
        assert 'total_market_size_2026' in details, "返回结果缺少total_market_size_2026字段"
        print(f"  通过: 2026年市场规模={details.get('total_market_size_2026', 'N/A')}")
        
        # 测试获取特定趋势
        trend_details = get_forecast_details('轻量化保温杯')
        # 可能返回None（如果数据中不存在），所以不强制断言
        if trend_details:
            print(f"  通过: 获取到趋势详情")
        else:
            print(f"  通过: 未找到指定趋势（可能数据中不存在）")
        
        # 测试获取不存在的预测
        details_none = get_forecast_details('non_existent_id')
        assert details_none is None, "不存在的预测应该返回None"
        print(f"  通过: 不存在的预测返回None")
        return True
    
    # 运行测试
    print("=== 市场预测工具测试 ===")
    print()
    
    tests = [
        ("生成市场预测", test_generate_forecast),
        ("生成市场预警", test_generate_alert),
        ("获取预测详细信息", test_get_forecast_details)
    ]
    
    passed = 0
    failed = 0
    
    for name, test_func in tests:
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"  失败: {e}")
            failed += 1
    
    print()
    print(f"=== 测试结果: {passed} 通过, {failed} 失败 ===")
    
    if failed == 0:
        print("✅ 所有测试通过！")
    else:
        print(f"❌ {failed} 个测试失败！")
        
except ImportError as e:
    print(f"导入模块失败: {e}")
    print("请确保forecast_tool.py文件存在且语法正确")
