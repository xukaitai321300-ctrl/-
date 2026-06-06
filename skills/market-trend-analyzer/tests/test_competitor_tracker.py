#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
竞争对手跟踪工具测试 - test_competitor_tracker.py
功能: 测试竞争对手跟踪工具的各项功能
"""

import sys
import os
import json

# 添加scripts目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scripts'))

try:
    from competitor_tracker import track_competitors, compare_competitors, get_competitor_details
    
    def test_track_competitors():
        """测试跟踪竞争对手功能"""
        print("测试: track_competitors()")
        result = track_competitors('膳魔师')
        assert result is not None, "跟踪竞争对手失败"
        assert 'name' in result, "返回结果缺少name字段"
        assert 'market_share' in result, "返回结果缺少market_share字段"
        print(f"  通过: 竞争对手={result['name']}, 市场份额={result.get('market_share', 'N/A')}%")
        return True
    
    def test_compare_competitors():
        """测试对比竞争对手功能"""
        print("测试: compare_competitors()")
        results = compare_competitors(['膳魔师', '虎牌', '象印'])
        assert isinstance(results, list), "返回结果应该是列表"
        assert len(results) > 0, "应该返回至少1个竞争对手"
        print(f"  通过: 对比了 {len(results)} 个竞争对手")
        return True
    
    def test_get_competitor_details():
        """测试获取竞争对手详细信息功能"""
        print("测试: get_competitor_details()")
        # 测试获取存在的竞争对手
        details = get_competitor_details('thermos')
        assert details is not None, "获取竞争对手详情失败"
        assert 'name' in details, "返回结果缺少name字段"
        print(f"  通过: 竞争对手名称={details['name']}, ID={details.get('id', 'N/A')}")
        
        # 测试获取不存在的竞争对手
        details_none = get_competitor_details('non_existent_id')
        assert details_none is None, "不存在的竞争对手应该返回None"
        print(f"  通过: 不存在的竞争对手返回None")
        return True
    
    # 运行测试
    print("=== 竞争对手跟踪工具测试 ===")
    print()
    
    tests = [
        ("跟踪竞争对手", test_track_competitors),
        ("对比竞争对手", test_compare_competitors),
        ("获取竞争对手详细信息", test_get_competitor_details)
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
    print("请确保competitor_tracker.py文件存在且语法正确")
