#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
市场趋势分析工具测试 - test_trend_analyzer.py
功能: 测试市场趋势分析工具的各项功能
"""

import sys
import os
import json

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scripts'))

try:
    from trend_analyzer import analyze_market_trend, identify_emerging_trends, get_trend_details
    
    def test_analyze_market_trend():
        """测试分析市场趋势功能"""
        print("测试: analyze_market_trend()")
        result = analyze_market_trend('2024-01', '2026-05')
        assert result is not None, "分析市场趋势失败"
        assert 'direction' in result, "返回结果缺少direction字段"
        assert 'market_heat' in result, "返回结果缺少market_heat字段"
        print(f"  通过: 趋势方向={result['direction']}, 市场热度={result['market_heat']}/10")
        return True
    
    def test_identify_emerging_trends():
        """测试识别新兴趋势功能"""
        print("测试: identify_emerging_trends()")
        trends = identify_emerging_trends()
        assert isinstance(trends, list), "返回结果应该是列表"
        assert len(trends) > 0, "应该识别出至少1个新兴趋势"
        print(f"  通过: 识别出 {len(trends)} 个新兴趋势")
        return True
    
    def test_get_trend_details():
        """测试获取趋势详细信息功能"""
        print("测试: get_trend_details()")
        # 测试获取存在的趋势
        details = get_trend_details('light_weight_design')
        assert details is not None, "获取趋势详情失败"
        assert 'name' in details, "返回结果缺少name字段"
        print(f"  通过: 趋势名称={details['name']}, 相关度={details.get('relevance', 'N/A')}")
        
        # 测试获取不存在的趋势
        details_none = get_trend_details('non_existent_id')
        assert details_none is None, "不存在的趋势应该返回None"
        print(f"  通过: 不存在的趋势返回None")
        return True
    
    # 运行测试
    print("=== 市场趋势分析工具测试 ===")
    print()
    
    tests = [
        ("分析市场趋势", test_analyze_market_trend),
        ("识别新兴趋势", test_identify_emerging_trends),
        ("获取趋势详细信息", test_get_trend_details)
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
    print("请确保trend_analyzer.py文件存在且语法正确")
