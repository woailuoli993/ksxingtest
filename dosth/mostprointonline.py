#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 2017/1/19

"""
## 1. 多线程解决连线问题
### > 问题：平面上有若干个点。点与点可以重合，寻找一条直线，使其能穿过最多的点。(好吧我承认这是我去面试时候的面试题。)
思路来自[这里][1]

> 平面上N个点以及这N个点构成的无向图，边数n(n-1)/2，对图遍历（深度或广度），遍历到某个点node的时候，计算该点与它的前一个点的斜率r，
用pr存储前一个点与它的前结点的斜率，如果pr！=r，则返回到node，继续遍历node的下一条边，如果斜率相等，则count++。如果找不到，
则从一下结点开始遍历未访问过的节点。
时间复杂度0(n^2)   悬而未决！！！！！！！！！！！！！！！！！！！
"""
from fractions import Fraction
from collections import deque


class Vertex(object):
    # 原生点 对象
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    __str__ = __repr__


class Edge(tuple):
    # 继承自建tuple类型并重写new方法
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return "Edge(%s, %s)" % (repr(self[0]), repr(self[1]))


class Graph(dict):

    def __init__(self, vs=[], es=[]):
        """ 建立一个新的图，(vs)为顶点vertices列表，(es)为边缘edges列表 """
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """ 添加顶点 v:  使用字典结构"""
        self[v] = {}

    def add_edge(self, e):
        """ 添加边缘 e: e 为一个元组(v,w)
            在两个顶点 w 和 v 之间添加成员e ，如果两个顶点之间已有边缘，则替换之 """
        v, w = e
        # 由于一条边会产生两个项目，因此该实现代表了一个无向图
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v1, v2):
        """ 接收两个顶点，则返回这条边，否则返回None """
        try:
            return self[v1][v2]
        except:
            return None

    def vertices(self):
        """ 返回图中所有顶点的列表 """
        return self.keys()

    def edges(self):
        """ 返回图中边的列表 """
        es = set()  # 为了避免返回重复的边，设为集合
        for v1 in self.vertices():
            for v2 in self.vertices():
                es.add(self.get_edge(v2, v1))

        es.discard(None)  # 若集合中存在None元素,则删除 无向图可以不用写这步
        return list(es)


    def add_all_edges(self, vs=None):
        """ 从一个无边的图开始，通过在各个顶点间添加边来生成一个完全图
            输入为目标顶点的列表，如果为None,则对所有的点进行全联结 """
        if vs is None:
            vs = self.vertices()
        for v1 in vs:
            for v2 in vs:
                if v1 is v2:
                    continue  # 假设不存在单顶点连通
                self.add_edge(Edge(v1, v2))

    def bfs(self):
        """
        广度优先搜索
        """
        # parents 记录所有可达节点与对应的父节点，这里是一个字典，我们将其 可达节点 作为 key，而将其 父节点 作为 value
        # query_queue 是用来存放待探索节点的 to-do 列表，这里是一个 FIFO

        node = self.vertices()[0]
        parents, query_queue = {node: None}, deque([node])

        while query_queue:
            # 总是从 FIFO 的左侧弹出待探索的节点
            q_node = query_queue.popleft()

            for neighbor in self.out_vertices(q_node):
                if neighbor in parents:
                    continue

                # 记录探索到的邻居节点及其父节点
                parents[neighbor] = q_node

                # 将其邻居节点推入 to-do 列表
                query_queue.append(neighbor)

        #如果想只得到点的话 可以
        # return prints.key()

        return parents

    def out_vertices(self, v):
        """ 接受一个Vertex并返回邻近顶点（通过一条边连接到给定节点的节点）的列表 """
        return self[v].keys()

    def out_edges(self, v):
        """ 接受一个Vertex并返回连接到给定节点的边的列表 """
        return self[v].values()


# 大佬的做法。 完全图 和广度优先真的很配啊。
class Solution:

    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        len_points = len(points)
        if len_points <= 1:
            return len_points
        max_count = 0
        for index1 in range(0, len_points):
            p1 = points[index1]
            gradients = {}
            infinite_count = 0
            duplicate_count = 0
            for index2 in range(index1, len_points):
                p2 = points[index2]
                dx = p2.x - p1.x
                dy = p2.y - p1.y
                if 0 == dx and 0 == dy:
                    duplicate_count += 1
                if 0 == dx:
                    infinite_count += 1
                else:
                    g = float(dy) / dx
                    gradients[g] = (gradients[g] + 1 if g in gradients else 1)
            if infinite_count > max_count:
                max_count = infinite_count
            for k, v in gradients.items():
                v += duplicate_count
                if v > max_count:
                    max_count = v
        return max_count


def getslope(print1, print2):
    if print2.y == print1.y and print1.x == print2.x:
        return None  # 重合点
    elif print1.x == print2.x:
        return 0  # 与y轴平行的线
    elif print1.y == print2.y:
        return "y"  # 与x轴平行的线
    else:
        return Fraction(print2.y-print1.y, print2.x-print1.x)  # 返回斜率

if __name__ == '__main__':
    # 给定一个点集 allprints
    allvertex = [Vertex(1, 1), Vertex(1, 2), Vertex(1, 3), Vertex(2, 1), Vertex(2, 2), Vertex(2, 3), Vertex(3, 1),
                 Vertex(3, 2), Vertex(3, 3), Vertex(2, 4)]

    # graph = Graph(allvertex)
    #
    # graph.add_all_edges()  # 生成无向完全图

    # print graph.bfs()

    sol = Solution()
    print sol.maxPoints(allvertex)

    # count = 1  # 初始化 最少线跟他本身共线 最少有一根
    # slope = None  # 初始化 斜率为None
    # for p_1 in range(len(allprints)):
    #     # print 'head %s |' % p_1,
    #     for p_2 in range(p_1+1, len(allprints)):
    #         # print p_2,
    #         # 到这里就可以生成n（n-1）／2 个边的无向图
    #         # 遍历边的斜率
    #         slope = getslope(p_1, p_2)  # 第一根线的斜率


