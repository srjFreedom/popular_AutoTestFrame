# -*- coding:utf8 -*-
"""
1.Repeated+int/str复合结构处理方法：
直接传递一个列表进来（使用extend()函数）
2.Repeated+message处理方法：
统计要传的message组数，根据组数做for循环
每个for循环开始使用add()方法得到一个RepeatedScalarFieldContainer类
再对类的变量赋值
"""

from protofile import accname_pb2
from protofile import achieve_pb2
from protofile import active_pb2
from protofile import arena_pb2
from protofile import chat_pb2
from protofile import compose_pb2
from protofile import draw_pb2
from protofile import dungeon_pb2
from protofile import exp_train_pb2
from protofile import friend_pb2
from protofile import goods_pb2
from protofile import guide_pb2
from protofile import mail_pb2
from protofile import major_pb2
from protofile import mcity_pb2
from protofile import partner_pb2
from protofile import pet_pb2
from protofile import player_pb2
from protofile import pve_pb2
from protofile import pvp_global_pb2
from protofile import pvp_pb2
from protofile import realtime_PVP_pb2
from protofile import rpc_pb2
from protofile import shop_pb2
from protofile import sign_pb2
from protofile import task_pb2
from protofile import trial_pb2
from protofile import wonderland_pb2

class C2S_ACCNAME():

    def c2s_login(self, paramlist):
        """
        登录协议
        :str accname: 登录账号
        :str sign: 签名，默认填写""
        """
        c2s = accname_pb2.c2s_login()
        c2s.accname = paramlist[0]
        c2s.sign = paramlist[1]
        return c2s

    def c2s_register(self, paramlist):
        """
        注册协议
        :str accname: 帐号
        :str nickname: 玩家名
        :str sign: 签名''
        :int major_id: 1,主角id
        """
        c2s = accname_pb2.c2s_register()
        c2s.accname = paramlist[0]
        c2s.nickname = paramlist[1]
        c2s.sign = paramlist[2]
        c2s.major_id = paramlist[3]
        return c2s

    def c2s_get_login_host(self):
        """
        获取网关ip和端口(多次发该协议会导致连接被断开)
        :param: 不需要参数
        """
        c2s = accname_pb2.c2s_get_login_host()
        return c2s

class C2S_ACHIEVE():

    def c2s_achieve_list(self):
        """
        获取成就列表
        :param:  不需要填写参数
        """
        c2s = achieve_pb2.c2s_achieve_list()
        return c2s

    def c2s_get_achieve_reward(self, paramlist):
        """
        领取成就奖励
        :achieveID:  成就ID
        """
        c2s = achieve_pb2.c2s_get_achieve_reward()
        c2s.achieveID = paramlist[0]
        return c2s

class C2S_ACTIVE():

    def c2s_get_choose_get_info(self):
        """
        获取活动信息
        :param:  不需要填写参数
        """
        c2s = active_pb2.c2s_get_choose_get_info()
        return c2s

    def c2s_choose_get_choose(self, paramlist):
        """
        选择活动奖励
        :int choose:  选项、选择的奖励
        """
        c2s = active_pb2.c2s_choose_get_choose()
        c2s.choose = paramlist[0]
        return c2s

    def c2s_get_choose_get_history(self):
        """
        获取奖励选择的历史记录
        :param:  不需要填写参数
        """
        c2s = active_pb2.c2s_get_choose_get_history()
        return c2s

class C2S_ARENA():

    def c2s_arena_camp(self, paramlist):
        """
        竞技场布阵
        :int major_id: 主角ID(必填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2-5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2-5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        。。。。。。（选填）
        """
        c2s = arena_pb2.c2s_arena_camp()
        c2s.formation.major_id = paramlist[0]
        partner = (len(paramlist) - 1)/2
        for i in xrange(partner):
            partner_pos = c2s.formation.partner_pos.add()
            partner_pos.partner_unique_id = paramlist[2*i+1]
            partner_pos.formation_pos = paramlist[2*i+2]
        return c2s

    def c2s_get_arena_info(self):
        """
        获取竞技场信息
        :param: 不需要参数
        """
        c2s = arena_pb2.c2s_get_arena_info()
        return c2s

    def c2s_get_arena_challenge_list(self, paramlist):
        """
        刷新竞技场对手信息
        :int is_refresh:  1.自己手动刷新 0.自动到时间刷新
        """
        c2s = arena_pb2.c2s_get_arena_challenge_list()
        c2s.is_refresh = paramlist[0]
        return c2s

    def c2s_arena_challenge(self, paramlist):
        """
        竞技场挑战
        :int challenge_player_id: 对手玩家ID
        :int challenge_rank: 对手排名
        :int camp_id: 对手主角ID（选填）
        :int camp_id: 对手伙伴ID（选填）
        。。。。。。
        """
        c2s = arena_pb2.c2s_arena_challenge()
        c2s.challenge_player_id = paramlist[0]
        c2s.challenge_rank = paramlist[1]
        if len(paramlist) > 2:
            c2s.camp_id_list.extend(paramlist[2:])
        return c2s

    def c2s_buy_arena_times(self):
        """
        购买挑战次数
        :param: 不需要参数
        """
        c2s = arena_pb2.c2s_buy_arena_times()
        return c2s

    def c2s_arena_first_rank_reward(self, paramlist):
        """
        领取首次达到排名奖励
        :int reward_id: 奖励id
        """
        c2s = arena_pb2.c2s_arena_first_rank_reward()
        c2s.reward_id = paramlist[0]
        return c2s

    def c2s_get_arena_shop(self):
        """
        获取竞技场商店信息
        :param: 不需要参数
        """
        c2s = arena_pb2.c2s_get_arena_shop()
        return c2s

    def c2s_buy_arena_product(self, paramlist):
        """
        购买竞技场商店商品
        :int pos: 商品位置
        """
        c2s = arena_pb2.c2s_buy_arena_product()
        c2s.pos = paramlist[0]
        return c2s

    def c2s_refresh_arena_shop(self):
        """
        刷新竞技场商店信息
        :param: 不需要参数
        """
        c2s = arena_pb2.c2s_refresh_arena_shop()
        return c2s

    def c2s_get_arena_log(self):
        """
        获取竞技场战斗记录
        :param: 不需要参数
        """
        c2s = arena_pb2.c2s_get_arena_log()
        return c2s

    def c2s_get_arena_rank(self, paramlist):
        """
        获取竞技场排名
        :int now_page: 当前页码
        """
        c2s = arena_pb2.c2s_get_arena_rank()
        c2s.now_page = paramlist[0]
        return c2s

    def c2s_get_arena_player_info(self, paramlist):
        """
        查看竞技场界面匹配的玩家信息
        :int player_id: 玩家UID
        """
        c2s = arena_pb2.c2s_get_arena_player_info()
        c2s.player_id = paramlist[0]
        return c2s

class C2S_CHAT():

    def c2s_world_chat(self, paramlist):
        """
        聊天，该协议没有对应的协议返回
        :str content: 聊天内容
        """
        c2s = chat_pb2.c2s_world_chat()
        c2s.content = paramlist[0]
        return c2s

class C2S_COMPOSE():

    def c2s_compose_partner(self, paramlist):
        """
        图纸合成伙伴
        :int goods_id: 图纸ID
        :int partner_unique_id_list: 伙伴UID
        :int partner_unique_id_list: 伙伴UID
        。。。
        """
        c2s = compose_pb2.c2s_compose_partner()
        c2s.goods_id = paramlist[0]
        if len(paramlist) > 1:
            c2s.partner_unique_id_list.extend(paramlist[1:])
        return c2s

    def c2s_compose_trump(self, paramlist):
        """
        法宝碎片合成法宝
        :int goods_id: 法宝碎片ID
        """
        c2s = compose_pb2.c2s_compose_trump()
        c2s.goods_id = paramlist[0]
        return c2s

class C2S_DRAW():

    def c2s_draw(self, paramlist):
        """
        抽卡
        :int pool_id: 1:灵符池 2 元宝池
        :int type: 抽取类型,1:单抽,10:10连抽
        注意：抽卡前需要有灵符或元宝
        """
        c2s = draw_pb2.c2s_draw()
        c2s.pool_id = paramlist[0]
        c2s.type = paramlist[1]
        return c2s

    def c2s_enter_draw(self):
        """
        前端告知后端进入了埋点界面
        :param: 不需要参数
        """
        c2s = draw_pb2.c2s_enter_draw()
        return c2s

class C2S_DUNGEON():

    def c2s_get_dungeon_info(self):
        """
        获取三千世界信息
        :param: 不需要参数
        """
        c2s = dungeon_pb2.c2s_get_dungeon_info()
        return c2s

    def c2s_challenge(self, paramlist):
        """
        挑战三千世界
        :int type_id: 类型ID
        :int pos: 难度
        """
        c2s = dungeon_pb2.c2s_challenge()
        c2s.type_id = paramlist[0]
        c2s.pos = paramlist[1]
        return c2s

    def c2s_save_formation(self, paramlist):
        """
        保存三千世界信息
        :int type_id: 类型ID
        :int major_id: 主角ID(必填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2-5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2-5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        。。。。。。（选填）
        """
        c2s = dungeon_pb2.c2s_save_formation()
        c2s.type_id = paramlist[0]
        c2s.formation.major_id = paramlist[1]
        partner = (len(paramlist) - 1)/2
        for i in xrange(partner):
            partner_pos = c2s.formation.partner_pos.add()
            partner_pos.partner_unique_id = paramlist[2*i + 2]
            partner_pos.formation_pos = paramlist[2*i + 3]
        return c2s

    def c2s_get_dungeon_time(self, paramlist):
        """
        单独获取时间
        :int type_id: 类型ID
        """
        c2s = dungeon_pb2.c2s_get_dungeon_time()
        c2s.type_id = paramlist[0]
        return c2s

    def c2s_buy_dungeon_challenge_count(self, paramlist):
        """
        三千世界购买挑战次数
        :int type_id: 购买的类型ID
        """
        c2s = dungeon_pb2.c2s_buy_dungeon_challenge_count()
        c2s.type_id = paramlist[0]
        return c2s

class C2S_EXP_TRAIN():

    def c2s_get_exp_train_info(self):
        """
        获取练功房信息
        :param: 不需要参数
        """
        c2s = exp_train_pb2.c2s_get_exp_train_info()
        return c2s

    def c2s_put_on(self, paramlist):
        """
        练功房上阵伙伴
        :int partner_unique_id: 伙伴UID
        :int pos: 练功房位置
        """
        c2s = exp_train_pb2.c2s_put_on()
        c2s.partner_unique_id = paramlist[0]
        c2s.pos = paramlist[1]
        return c2s

    def c2s_collect_train(self, paramlist):
        """
        练功房收获
        :int collect_list: 收获的位置
        :int collect_list: 收获的位置（选填）
        。。。。。。（选填）
        """
        c2s = exp_train_pb2.c2s_collect_train()
        c2s.collect_list.extend(paramlist)
        return c2s

    def c2s_gold_unlock(self, paramlist):
        """
        练功房元宝解锁
        :int pos: 元宝解锁槽位
        """
        c2s = exp_train_pb2.c2s_gold_unlock()
        c2s.pos = paramlist[0]
        return c2s

    def c2s_buy_double_time(self, paramlist):
        """
        练功房双倍经验
        :int type_id: 1.双倍 2.单倍
        """
        c2s = exp_train_pb2.c2s_buy_double_time()
        c2s.type_id = paramlist[0]
        return c2s

class C2S_FRIEND():

    def c2s_get_friend_list(self):
        """
        获取好友信息
        :param: 不需要参数
        """
        c2s = friend_pb2.c2s_get_friend_list()
        return c2s

    def c2s_check_nickname_exists(self, paramlist):
        """
        检测玩家是否存在
        :str nickname: 玩家昵称
        """
        c2s = friend_pb2.c2s_check_nickname_exists()
        c2s.nickname = paramlist[0]
        return c2s

    def c2s_friend_apply(self, paramlist):
        """
        申请加好友
        :str nickname: 玩家昵称
        """
        c2s = friend_pb2.c2s_friend_apply()
        c2s.nickname = paramlist[0]
        return c2s

    def c2s_get_friend_apply_list(self):
        """
        获取好友申请列表
        :param: 不需要参数
        """
        c2s = friend_pb2.c2s_get_friend_apply_list()
        return c2s

    def c2s_friend_apply_agree_reply(self, paramlist):
        """
        同意申请加好友
        :int apply_id: 申请玩家甲id（必填）
        :int apply_id: 申请玩家乙id（可选）
        :int apply_id: 申请玩家丙id（可选）
        :int apply_id: 申请玩家丁id（可选）
        。。。。。。（可选）
        """
        c2s = friend_pb2.c2s_friend_apply_agree_reply()
        c2s.apply_id_list.extend(paramlist)
        return c2s

    def c2s_friend_apply_reject_reply(self, paramlist):
        """
        拒绝或者忽略加好友
        :int op: 1.拒绝 2.全部忽略
        :int apply_id: 申请玩家甲id（必填）
        :int apply_id: 申请玩家乙id（可选）
        :int apply_id: 申请玩家丙id（可选）
        :int apply_id: 申请玩家丁id（可选）
        。。。。。。（可选）
        """
        c2s = friend_pb2.c2s_friend_apply_reject_reply()
        c2s.op = paramlist[0]
        if len(paramlist) > 1:
            c2s.apply_id_list.extend(paramlist[1:])
        return c2s

    def c2s_friend_del(self, paramlist):
        """
        删除好友
        :int friend_id: 好友UID
        """
        c2s = friend_pb2.c2s_friend_del()
        c2s.friend_id = paramlist[0]
        return c2s

    def c2s_friend_donate(self, paramlist):
        """
        捐赠体力
        :int friend_id: 好友UID
        """
        c2s = friend_pb2.c2s_friend_donate()
        c2s.friend_id = paramlist[0]
        return c2s

class C2S_GOODS():

    def c2s_goods_list(self):
        """
        获取背包信息
        :param: 不需要参数
        """
        c2s = goods_pb2.c2s_goods_list()
        return c2s

    def c2s_trump_up_lv(self, paramlist):
        """
        法宝升级
        :int id: 法宝物品UID
        :int cost_id_list: 消耗物品UID
        """
        c2s = goods_pb2.c2s_trump_up_lv()
        c2s.id = paramlist[0]
        c2s.cost_id_list.extend(paramlist[1:])
        return c2s

    def c2s_trump_equip(self, paramlist):
        """
        法宝装备到伙伴上
        :int id: 法宝物品UID
        :int partner_unique_id: 伙伴UID
        """
        c2s = goods_pb2.c2s_trump_equip()
        c2s.id = paramlist[0]
        c2s.partner_unique_id = paramlist[1]
        return c2s

    def c2s_trump_unequip(self, paramlist):
        """
        法宝从伙伴上脱下
        :int id: 法宝物品UID
        """
        c2s = goods_pb2.c2s_trump_unequip()
        c2s.id = paramlist[0]
        return c2s

    def c2s_goods_sell(self, paramlist):
        """
        出售物品
        :int id: 物品UID
        :int num: 物品数量
        """
        c2s = goods_pb2.c2s_goods_sell()
        c2s.id = paramlist[0]
        c2s.num = paramlist[1]
        return c2s

    def c2s_goods_use(self, paramlist):
        """
        使用物品
        :int id: 物品UID
        :int num: 物品数量
        """
        c2s = goods_pb2.c2s_goods_use()
        c2s.id = paramlist[0]
        c2s.num = paramlist[1]
        return c2s

class C2S_GUDIE():

    def c2s_update_system_active(self, paramlist):
        """
        激活系统协议
        :int id: 激活系统ID
        :int effect: 不知道是啥
        :int id: 激活系统ID
        :int effect: 不知道是啥
        。。。。。。
        """
        c2s = guide_pb2.c2s_update_system_active()
        activelen = len(paramlist)/2
        for i in xrange(activelen):
            actives = c2s.actives.add()
            actives.id = paramlist[2*i]
            actives.effect = paramlist[2*i+1]
        return c2s

    def c2s_update_guides(self, paramlist):
        """
        提交引导信息
        :int id: 引导ID
        :str state: 引导状态
        :int id: 引导ID
        :str state: 引导状态
        。。。。。。
        """
        c2s = guide_pb2.c2s_update_guides()
        guidelen = len(paramlist)/2
        for i in xrange(guidelen):
            guide1 = c2s.guide1.add()
            guide1.id = paramlist[2*i]
            guide1.state = paramlist[2*i+1]
        return c2s

    def c2s_download_guide_info(self):
        """
        下载引导信息
        :param: 不需要填参数
        """
        c2s = guide_pb2.c2s_download_guide_info()
        return c2s

    def c2s_guides_changed(self, paramlist):
        """
        告诉后端完成的引导
        :int id: 32
        """
        c2s = guide_pb2.c2s_guides_changed()
        c2s.id = paramlist[0]
        return c2s

class C2S_MAIL():

    def c2s_mail_list(self):
        """
        获取邮件列表
        :param: 不需要填参数
        """
        c2s = mail_pb2.c2s_mail_list()
        return c2s

    def c2s_read_mail(self, paramlist):
        """
        更新邮件列表
        :int mail_id: 邮件ID
        :int mail_id: 邮件ID（选填）
        。。。。。。（选填）
        """
        c2s = mail_pb2.c2s_read_mail()
        c2s.mail_id.extend(paramlist)
        return c2s

    def c2s_get_mail_rewards(self, paramlist):
        """
        领取邮件奖励
        :int mail_id: 邮件ID
        :int mail_id: 邮件ID（选填）
        。。。。。。（选填）
        """
        c2s = mail_pb2.c2s_get_mail_rewards()
        c2s.mail_ids.extend(paramlist)
        return c2s

    # 目前没有删除邮件的协议
    # def c2s_delete_mails(self, paramlist):
    #     """
    #     删除邮件
    #     :int mail_id: 邮件ID
    #     :int mail_id: 邮件ID（选填）
    #     :int mail_id: 邮件ID（选填）
    #     。。。。。。（选填）
    #     """
    #     c2s = mail_pb2.c2s_delete_mails()
    #     c2s.mail_ids.extend(paramlist)
    #     return c2s


class C2S_MAJOR():

    def c2s_get_major_list(self):
        """
        获取主角列表
        :param: 不需要填参数
        """
        c2s = major_pb2.c2s_get_major_list()
        return c2s

    def c2s_major_switch(self, paramlist):
        """
        主角切换
        :int major_id: 主角ID
        """
        c2s = major_pb2.c2s_major_switch()
        c2s.major_id = paramlist[0]
        return c2s

    def c2s_major_skill_switch(self, paramlist):
        """
        技能切换
        :int major_id: 主角ID
        :int pos: 技能位置
        :int skill_id: 技能ID
        """
        c2s = major_pb2.c2s_major_skill_switch()
        c2s.major_id = paramlist[0]
        c2s.pos = paramlist[1]
        c2s.skill_id = paramlist[2]
        return c2s

    def c2s_major_switch_skin(self, paramlist):
        """
        穿戴皮肤
        :int skin_id: 皮肤id
        """
        c2s = major_pb2.c2s_major_switch_skin()
        c2s.skin_id = paramlist[0]
        return c2s

class C2S_MCITY():

    def c2s_get_mcity_info(self):
        """
        获取自己主城信息
        :param: 不需要填参数
        """
        c2s = mcity_pb2.c2s_get_mcity_info()
        return c2s

    def c2s_get_mcity_build_info(self, paramlist):
        """
        查看某个建筑的信息
        :int build_id: 建筑ID
        """
        c2s = mcity_pb2.c2s_get_mcity_info()
        c2s.build_id = paramlist[0]
        return c2s

    def c2s_mcity_exit(self):
        """
        退出（退出自己主城/或者其他玩家的主城）
        :param: 不需要填参数
        """
        c2s = mcity_pb2.c2s_mcity_exit()
        return c2s

    def c2s_mcity_avatar(self, paramlist):
        """
        装扮自己的主城
        :int avatar_id: 装扮id
        """
        c2s = mcity_pb2.c2s_mcity_avatar()
        c2s.avatar_id = paramlist[0]
        return c2s

    def c2s_mcity_collect(self, paramlist):
        """
        收取灵石/碎片
        :int build_id: 建筑ID
        """
        c2s = mcity_pb2.c2s_mcity_collect()
        c2s.build_id = paramlist[0]
        return c2s

    def c2s_mcity_set_defence(self, paramlist):
        """
        设置防守
        :int defence_info: 建筑ID
        """
        c2s = mcity_pb2.c2s_mcity_set_defence()
        c2s.defence_info.major_id = paramlist[0]
        c2s.defence_info.partner_unique_id_list.extend(paramlist[1:])
        return c2s

    def c2s_mcity_clear_damaged(self, paramlist):
        """
        清除破损状态
        :int build_id: 建筑ID
        """
        c2s = mcity_pb2.c2s_mcity_clear_damaged()
        c2s.build_id = paramlist[0]
        return c2s

    def c2s_mcity_buy_avatar(self, paramlist):
        """
        购买扮装
        :int avatar_id: 装扮id
        """
        c2s = mcity_pb2.c2s_mcity_buy_avatar()
        c2s.avatar_id = paramlist[0]
        return c2s

    def c2s_get_mcity_rob_list(self, paramlist):
        """
        获取掠夺列表
        :int goods_id: 碎片id
        """
        c2s = mcity_pb2.c2s_get_mcity_rob_list()
        c2s.goods_id = paramlist[0]
        return c2s

    def c2s_mcity_refresh_rob_list(self, paramlist):
        """
        刷新掠夺列表
        :int goods_id: 碎片id
        """
        c2s = mcity_pb2.c2s_mcity_refresh_rob_list()
        c2s.goods_id = paramlist[0]
        return c2s

    def c2s_get_other_mcity_info(self, paramlist):
        """
        获取目标玩家主城信息
        :int obj_player_id: 目标玩家id
        """
        c2s = mcity_pb2.c2s_get_other_mcity_info()
        c2s.obj_player_id = paramlist[0]
        return c2s

    def c2s_get_mcity_log_list(self):
        """
        获取主城日志列表
        :param: 不需要填参数
        """
        c2s = mcity_pb2.c2s_get_mcity_log_list()
        return c2s

    def c2s_mcity_rob(self, paramlist):
        """
        掠夺
        :int obj_player_id:  目标玩家id
        :int goods_id:  掠夺法宝碎片id
        """
        c2s = mcity_pb2.c2s_mcity_rob()
        c2s.obj_player_id = paramlist[0]
        c2s.goods_id = paramlist[1]
        return c2s

    def c2s_mcity_rob_battle(self, paramlist):
        """
        掠夺战斗结果
        :int obj_player_id:  目标玩家id
        :int goods_id:  掠夺法宝碎片id
        :int result:  1.攻击方胜利 2：防守方胜利
        """
        c2s = mcity_pb2.c2s_mcity_rob()
        c2s.obj_player_id = paramlist[0]
        c2s.goods_id = paramlist[1]
        c2s.result = paramlist[2]
        return c2s

    def c2s_mcity_revenge(self, paramlist):
        """
        发起复仇
        :int log_id:  日志唯一id
        """
        c2s = mcity_pb2.c2s_mcity_revenge()
        c2s.log_id = paramlist[0]
        return c2s

    def c2s_mcity_revenge_battle(self, paramlist):
        """
        复仇结果
        :int log_id:  日志唯一id
        :int result:  1.攻击方胜利 2：防守方胜利
        """
        c2s = mcity_pb2.c2s_mcity_revenge_battle()
        c2s.log_id = paramlist[0]
        c2s.result = paramlist[1]
        return c2s

class C2S_PARTNER():

    def c2s_get_partner_list(self):
        """
        获取伙伴列表
        :param: 不需要填参数
        """
        c2s = partner_pb2.c2s_get_partner_list()
        return c2s

    def c2s_partner_up_lv(self, paramlist):
        """
        吞噬升级
        :int id: 需要升级的伙伴唯一id
        :int cost_id: 升级消耗的伙伴id
        :int cost_id: 升级消耗的伙伴id（选填）
        :int cost_id: 升级消耗的伙伴id（选填）
        。。。。。。（选填）
        """
        c2s = partner_pb2.c2s_partner_up_lv()
        c2s.id = paramlist[0]
        c2s.cost_id_list.extend(paramlist[1:])
        return c2s

    def c2s_partner_up_star(self, paramlist):
        """
        伙伴升星
        :int id: 需要升星的伙伴唯一id
        :int cost_id: 升星消耗的伙伴id
        :int cost_id: 升星消耗的伙伴id（选填）
        :int cost_id: 升星消耗的伙伴id（选填）
        。。。。。。（选填）
        """
        c2s = partner_pb2.c2s_partner_up_star()
        c2s.id = paramlist[0]
        c2s.cost_id_list.extend(paramlist[1:])
        return c2s

    def c2s_partner_wake(self, paramlist):
        """
        吞噬升级
        :int id: 需要觉醒的id
        """
        c2s = partner_pb2.c2s_partner_wake()
        c2s.id = paramlist[0]
        return c2s

    def c2s_partner_switch_skin(self, paramlist):
        """
        切换皮肤
        :int id: 伙伴唯一id
        :int skin_id: 皮肤id
        """
        c2s = partner_pb2.c2s_partner_switch_skin()
        c2s.id = paramlist[0]
        c2s.skin_id = paramlist[1]
        return c2s

    def c2s_partner_lock(self, paramlist):
        """
        加锁/解除锁定
        :int id: 伙伴唯一id
        :int op:  1.加锁 0.解锁
        """
        c2s = partner_pb2.c2s_partner_lock()
        c2s.id = paramlist[0]
        c2s.op = paramlist[1]
        return c2s

class C2S_PET():

    def c2s_get_pet_list(self):
        """
        获取灵宠列表
        :param: 不需要填参数
        """
        c2s = pet_pb2.c2s_get_pet_list()
        return c2s

    def c2s_pet_switch(self, paramlist):
        """
        切换灵宠
        :int id: 灵宠唯一id
        """
        c2s = pet_pb2.c2s_pet_switch()
        c2s.id = paramlist[0]
        return c2s

    def c2s_pet_up_lv(self, paramlist):
        """
        吃法宝升级灵宠
        :int id: 灵宠唯一id
        :int cost_id: 法宝唯一id
        :int cost_id: 法宝唯一id（选填）
        :int cost_id: 法宝唯一id（选填）
        。。。。。。 （选填）
        """
        c2s = pet_pb2.c2s_pet_up_lv()
        c2s.id = paramlist[0]
        c2s.cost_id_list.extend(paramlist[1:])
        return c2s

class C2S_PLAYER():

    def c2s_game_loaded(self):
        """
        玩家登录/重连游戏加载完成
        :param: 不需要填参数
        """
        c2s = player_pb2.c2s_game_loaded()
        return c2s

    def c2s_get_player_info(self):
        """
        获取玩家信息
        :param: 不需要填参数
        """
        c2s = player_pb2.c2s_get_player_info()
        return c2s

    def c2s_heart_check(self):
        """
        心跳包
        :param: 不需要填参数
        """
        c2s = player_pb2.c2s_heart_check()
        return c2s

    def c2s_red_tip(self):
        """
        红点提示
        :param: 不需要填参数
        """
        c2s = player_pb2.c2s_red_tip()
        return c2s

    def c2s_get_buy_energy_count(self):
        """
        获取已购买体力的次数
        :param: 不需要填参数
        """
        c2s = player_pb2.c2s_get_buy_energy_count()
        return c2s

    def c2s_buy_energy(self):
        """
        购买体力
        :param: 不需要填参数
        """
        c2s = player_pb2.c2s_buy_energy()
        return c2s

class C2S_PVE():

    def c2s_upload_pve(self, paramlist):
        """
        上传PVE信息
        :int trigger_id:  触发器ID
        :int trigger_id:  触发器ID（选填）
        :int trigger_id:  触发器ID（选填）
        。。。。。。（选填）
        """
        c2s = pve_pb2.c2s_upload_pve()
        c2s.trigger_ids.extend(paramlist)
        return c2s

    def c2s_download_pve(self):
        """
        下载PVE信息
        :param:  不需要参数
        """
        c2s = pve_pb2.c2s_download_pve()
        return c2s

    def c2s_upload_pve_player_pos(self, paramlist):
        """
        上传PVE场景主角位置
        :int pos:  位置
        """
        c2s = pve_pb2.c2s_upload_pve_player_pos()
        c2s.pos = paramlist[0]
        return c2s

    def c2s_upload_pve_object_state(self, paramlist):
        """
        上传PVE场景物件状态
        :int id:  状态ID
        :int pos: 位置
        :int dir: 不知道是啥
        :int create_or_destroy: 1 是 0 否
        """
        c2s = pve_pb2.c2s_upload_pve_object_state()
        list1 = c2s.list.add()
        list1.id = paramlist[0]
        list1.pos = paramlist[1]
        list1.dir = paramlist[2]
        list1.create_or_destroy = paramlist[3]
        return c2s

    def c2s_download_pve_state(self):
        """
        下载PVE场景状态
        :param:  不需要填写参数
        """
        c2s = pve_pb2.c2s_download_pve_state()
        return c2s

    def c2s_pve_battle_reward(self, paramlist):
        """
        领取pve战斗奖励
        :int battle:  战斗ID
        """
        c2s = pve_pb2.c2s_pve_battle_reward()
        c2s.battle = paramlist[0]
        return c2s

class C2S_PVP():

    def c2s_pvp_loading_progress(self, paramlist):
        """
        告诉服务器加载进度
        :int progress: 万分位
        """
        c2s = pvp_pb2.c2s_pvp_loading_progress()
        c2s.progress = paramlist[0]
        return c2s

    def c2s_pvp_loading_complete(self):
        """
        告诉服务器加载完成
        :param: 不需要填参数
        """
        c2s = pvp_pb2.c2s_pvp_loading_complete()
        return c2s

    def c2s_pvp_battle_command(self, paramlist):
        """
        战斗指令
        :int releaser_battle_id: 发布战斗ID
        :int skill_id: 技能ID
        :int click_target_battle_id: 点选的目标战斗ID
        :int client_index: 当前客户端的随机数下标，只要填写大于100的数就没有问题
        :int target_battle_id: 实际的目标战斗ID
        :int target_battle_id: 实际的目标战斗ID（选填）
        :int target_battle_id: 实际的目标战斗ID（选填）
        。。。。。。（选填）
        """
        c2s = pvp_pb2.c2s_pvp_battle_command()
        c2s.releaser_battle_id = paramlist[0]
        c2s.skill_id = paramlist[1]
        c2s.click_target_battle_id = paramlist[2]
        c2s.client_index = paramlist[3]
        c2s.target_battle_ids.extend(paramlist[4:])
        return c2s

    # def c2s_pvp_reconnect(self, paramlist):
    #     """
    #     断线重连PVP服务
    #     :int srv_pvp_id: 请求重连的PVP服务id, 为了防止请求重连的pvp服务不一致问题
    #     """
    #     c2s = pvp_pb2.c2s_pvp_reconnect()
    #     c2s.srv_pvp_id = paramlist[0]
    #     return c2s

    def c2s_pvp_autofight(self, paramlist):
        """
        自动战斗
        :int is_auto: 1.自动战斗
        """
        c2s = pvp_pb2.c2s_pvp_autofight()
        c2s.is_auto = paramlist[0]
        return c2s

    def c2s_pvp_quit(self):
        """
        主动退出战斗
        :param: 不需要填参数
        """
        c2s = pvp_pb2.c2s_pvp_quit()
        return c2s

    def c2s_pvp_record(self, paramlist):
        """
        请求录像
        :int reocord_id: 录像ID
        """
        c2s = pvp_pb2.c2s_pvp_record()
        c2s.reocord_id = paramlist[0]
        return c2s

    def c2s_pvp_change_speed(self, paramlist):
        """
        改变战斗速度
        :int speed: 战斗速度
        """
        c2s = pvp_pb2.c2s_pvp_change_speed()
        c2s.speed = paramlist[0]
        return c2s

    def c2s_pvp_change_focus(self, paramlist):
        """
        改变集火目标
        :int speed: 集火目标
        """
        c2s = pvp_pb2.c2s_pvp_change_focus()
        c2s.battle_id = paramlist[0]
        return c2s

    # def c2s_pvp_complete(self, paramlist):
    #     """
    #     战斗完成
    #     :int is_win: 1.胜利 2.失败
    #     """
    #     c2s = pvp_pb2.c2s_pvp_complete()
    #     c2s.is_win = paramlist[0]
    #     return c2s

class C2S_PVP_GOLOBAL():

    def c2s_pvp_global_join(self, paramlist):
        """
        请求加入pvp等待
        :int id: 主角或者伙伴id
        :int pos: 所站位置
        :int type: 主角还是伙伴 1: 主角 2: 伙伴
        :int id: 主角或者伙伴id（选填）
        :int pos: 所站位置（选填）
        :int type: 主角还是伙伴 1: 主角 2: 伙伴（选填）
        。。。。。。（选填）
        """
        c2s = pvp_global_pb2.c2s_pvp_global_join()
        poselen = len(paramlist)/3
        for i in xrange(poselen):
            pvp_pose = c2s.pvp_poses.add()
            pvp_pose.id = paramlist[3*i]
            pvp_pose.pos = paramlist[3*i+1]
            pvp_pose.type = paramlist[3*i+2]
        return c2s

    def c2s_pvp_global_leav(self, paramlist):
        """
        请求离开pvp等待
        :param:  不需要参数
        """
        c2s = pvp_global_pb2.c2s_pvp_global_leav()
        return c2s

class C2S_REALTIME_PVP():

    def c2s_get_realtime_pvp_state(self):
        """
        获取实时pvp状态
        :param:  不需要参数
        """
        c2s = realtime_PVP_pb2.c2s_get_realtime_pvp_state()
        return c2s

    def c2s_get_realtime_pvp_info(self):
        """
        获取活动信息
        :param:  不需要参数
        """
        c2s = realtime_PVP_pb2.c2s_get_realtime_pvp_info()
        return c2s

    def c2s_get_realtime_pvp_rank(self, paramlist):
        """
        获取实时pvp排名
        :int page:  页码数
        """
        c2s = realtime_PVP_pb2.c2s_get_realtime_pvp_rank()
        c2s.page = paramlist[0]
        return c2s

    def c2s_realtime_pvp_sign(self):
        """
        实时pvp签到
        :param:  不需要参数
        """
        c2s = realtime_PVP_pb2.c2s_realtime_pvp_sign()
        return c2s

    def c2s_realtime_pvp_match(self):
        """
        实时pvp匹配
        :param:  不需要参数
        """
        c2s = realtime_PVP_pb2.c2s_realtime_pvp_match()
        return c2s

    def c2s_realtime_pvp_cancel_match(self):
        """
        实时pvp取消匹配
        :param:  不需要参数
        """
        c2s = realtime_PVP_pb2.c2s_realtime_pvp_cancel_match()
        return c2s

    def c2s_realtime_pvp_camp(self, paramlist):
        """
        实时pvp阵容设置
        :int major_id: 主角ID(必填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2-5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2-5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        。。。。。。（选填）
        """
        c2s = realtime_PVP_pb2.c2s_realtime_pvp_camp()
        c2s.formation.major_id = paramlist[0]
        partner = (len(paramlist) - 1)/2
        for i in xrange(partner):
            partner_pos = c2s.formation.partner_pos.add()
            partner_pos.partner_unique_id = paramlist[2*i + 1]
            partner_pos.formation_pos = paramlist[2*i + 2]
        return c2s

    def c2s_realtime_pvp_get_base_info(self, paramlist):
        """
        获取实时pvp玩家基本信息
        :int playerID:  玩家UID
        """
        c2s = realtime_PVP_pb2.c2s_realtime_pvp_get_base_info()
        c2s.playerID = paramlist[0]
        return c2s

class C2S_SHOP():

    def c2s_get_products(self, paramlist):
        """
        获取商品列表
        :int version: 版本号，填1即可
        """
        c2s = shop_pb2.c2s_get_products()
        c2s.version = paramlist[0]
        return c2s

    def c2s_buy_product(self, paramlist):
        """
        获取商品列表
        :int version: 版本号，填2
        :int product_id: 商品ID
        :int key: 前端需要,默认填0 不清楚啥意思
        :int num: 数量，默认填1
        """
        c2s = shop_pb2.c2s_buy_product()
        c2s.version = paramlist[0]
        c2s.product_id = paramlist[1]
        c2s.key = paramlist[2]
        c2s.num = paramlist[3]
        return c2s

class C2S_SIGN():

    def c2s_get_sign_info(self):
        """
        获取签到信息
        :param:  不需要填写参数
        """
        c2s = sign_pb2.c2s_get_sign_info()
        return c2s

    def c2s_sign(self):
        """
        进行签到
        :param:  不需要填写参数
        """
        c2s = sign_pb2.c2s_sign()
        return c2s

class C2S_TASK():

    def c2s_save_pve_task(self, paramlist):
        """
        上传完整剧情任务
        :int task_id: 主线任务ID
        :int task_state: 主线任务状态，1.不可接 2.可接未接 3.已接未完成 4.已经完成
        :int task_id: 支线任务ID（选填）
        :int task_state: 支线任务状态，1.不可接 2.可接未接 3.已接未完成 4.已经完成（选填）
        :int task_id: 支线任务ID（选填）
        :int task_state: 支线任务状态，1.不可接 2.可接未接 3.已接未完成 4.已经完成（选填）
        。。。。。。（选填）
        """
        c2s = task_pb2.c2s_save_pve_task()
        c2s.main_task.task_id = paramlist[0]
        c2s.main_task.task_state = paramlist[1]
        tasklen = (len(paramlist) - 2) / 2
        for i in xrange(tasklen):
            sub_task_list = c2s.sub_task_list.add()
            sub_task_list.task_id = paramlist[2*i+2]
            sub_task_list.task_state = paramlist[2*i+3]
        return c2s

    def c2s_update_pve_task(self, paramlist):
        """
        上传增量剧情任务
        :int task_id: 主线任务ID
        :int task_state: 主线任务状态，1.不可接 2.可接未接 3.已接未完成 4.已经完成
        :int task_id: 支线任务ID（选填）
        :int task_state: 支线任务状态，1.不可接 2.可接未接 3.已接未完成 4.已经完成（选填）
        :int task_id: 支线任务ID（选填）
        :int task_state: 支线任务状态，1.不可接 2.可接未接 3.已接未完成 4.已经完成（选填）
        。。。。。。（选填）
        """
        c2s = task_pb2.c2s_update_pve_task()
        c2s.main_task.task_id = paramlist[0]
        c2s.main_task.task_state = paramlist[1]
        tasklen = (len(paramlist) - 2) / 2
        for i in xrange(tasklen):
            sub_task_list = c2s.sub_task_list.add()
            sub_task_list.task_id = paramlist[2*i+2]
            sub_task_list.task_state = paramlist[2*i+3]
        return c2s

    def c2s_load_pve_task(self):
        """
        下载同步剧情任务
        :param:  不需要填写参数
        """
        c2s = task_pb2.c2s_load_pve_task()
        return c2s

    def c2s_get_daily_task_list(self):
        """
        获取日常任务列表
        :param:  不需要填写参数
        """
        c2s = task_pb2.c2s_get_daily_task_list()
        return c2s

    def c2s_task_daily_reward(self, paramlist):
        """
        领取日常任务奖励
        :int task_id:  任务ID
        """
        c2s = task_pb2.c2s_task_daily_reward()
        c2s.task_id = paramlist[0]
        return c2s

    def c2s_task_daily_active_reward(self, paramlist):
        """
        领取日常任务活跃度奖励
        :int task_id:  任务ID
        """
        c2s = task_pb2.c2s_task_daily_active_reward()
        c2s.active_id = paramlist[0]
        return c2s

    def c2s_task_secret_reward(self, paramlist):
        """
        秘闻领奖
        :int id:  秘闻id
        """
        c2s = task_pb2.c2s_task_secret_reward()
        c2s.id = paramlist[0]
        return c2s

    def c2s_get_task_secret_reward(self):
        """
        获取秘闻奖励状态
        :param:  不需要填写参数
        """
        c2s = task_pb2.c2s_get_task_secret_reward()
        return c2s

    def c2s_get_story_branch(self):
        """
        获取支线剧情列表
        :param:  不需要填写参数
        """
        c2s = task_pb2.c2s_get_story_branch()
        return c2s

    def c2s_update_story_list(self, paramlist):
        """
        增量更新支线剧情列表
        :int id: 支线剧情id
        :str progress: 进度
        :int state: 状态 1.不可接 2.可接未接 3.已接未完成 4.已经完成
        :int id: 支线剧情id （选填）
        :str progress: 进度（选填）
        :int state: 状态 1.不可接 2.可接未接 3.已接未完成 4.已经完成（选填）
        。。。。。。（选填）
        """
        c2s = task_pb2.c2s_update_story_list()
        tasklen = (len(paramlist)) / 3
        for i in xrange(tasklen):
            story_list = c2s.story_list.add()
            story_list.id = paramlist[3*i]
            story_list.progress = paramlist[3*i + 1]
            story_list.state = paramlist[3*i + 2]
        return c2s

    def c2s_update_story_data_list(self, paramlist):
        """
        增量提交支线剧情数据
        :int id: 数据id（物品，伙伴等）
        :int type: 数据类型(1.物品 2.伙伴)
        :int num: 数量
        :int append: 追加参数，默认填0，不知道啥意思
        :int id: 数据id（物品，伙伴等）（选填）
        :int type: 数据类型(1.物品 2.伙伴)（选填）
        :int num: 数量（选填）
        :int append: 追加参数，默认填0，不知道啥意思（选填）
        。。。。。。（选填）
        """
        c2s = task_pb2.c2s_update_story_data_list()
        tasklen = (len(paramlist)) / 4
        for i in xrange(tasklen):
            data_list = c2s.data_list.add()
            data_list.id = paramlist[4*i]
            data_list.type = paramlist[4*i + 1]
            data_list.num = paramlist[4*i + 2]
            data_list.append = paramlist[4*i + 3]
        return c2s


class C2S_TRIAL():

    def c2s_trial_register(self, paramlist):
        """
        报名参与试练副本
        :int trial_id: 试练副本id
        :int major_id: 主角id
        :int partner_unique_id: 伙伴UID（必填）
        :int partner_unique_id: 伙伴UID（选填）
        。。。。。。（选填）
        """
        c2s = trial_pb2.c2s_trial_register()
        c2s.trial_id = paramlist[0]
        c2s.major_id = paramlist[1]
        if len(paramlist) > 2:
            c2s.partner_unique_id_list.extend(paramlist[2:])
        return c2s

    def c2s_trial_reconnect(self, paramlist):
        """
        试炼副本重连
        :int trial_id: 试练副本id
        """
        c2s = trial_pb2.c2s_trial_reconnect()
        c2s.trial_id = paramlist[0]
        return c2s

    def c2s_trial_next_floor(self, paramlist):
        """
        请求进入下一层
        :int trial_id: 试练副本id
        :int floor: 层数
        """
        c2s = trial_pb2.c2s_trial_next_floor()
        c2s.trial_id = paramlist[0]
        c2s.floor = paramlist[1]
        return c2s

    def c2s_trial_open_box(self, paramlist):
        """
        开启宝箱
        :int trial_id: 试练副本id
        :int pos: 节点位置
        :int use_seal: 是否使用起封符，0.不使用，1.使用
        """
        c2s = trial_pb2.c2s_trial_open_box()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        c2s.use_seal = paramlist[2]
        return c2s

    def c2s_trial_buji(self, paramlist):
        """
        请求补给（必须先打完前面节点的小怪才能触发）
        :int trial_id: 试练副本id
        :int pos: 节点位置
        """
        c2s = trial_pb2.c2s_trial_buji()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        return c2s

    def c2s_trial_jiachi(self, paramlist):
        """
        触发加持（必须先打完前面节点的小怪才能触发）
        :int trial_id: 试练副本id
        :int pos: 节点位置
        """
        c2s = trial_pb2.c2s_trial_jiachi()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        return c2s

    def c2s_trial_jiachi_select(self, paramlist):
        """
        选择加持套装
        :int trial_id: 试练副本id
        :int pos: 节点位置
        :int buff_id: 加持id，默认是0
        """
        c2s = trial_pb2.c2s_trial_jiachi_select()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        c2s.buff_id = paramlist[2]
        return c2s

    def c2s_trial_shop_list(self, paramlist):
        """
        获取商人列表
        :int trial_id: 试练副本id
        :int pos: 节点位置
        """
        c2s = trial_pb2.c2s_trial_shop_list()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        return c2s

    def c2s_trial_shop_buy(self, paramlist):
        """
        商人购买
        :int trial_id: 试练副本id
        :int pos: 节点位置
        :int index: 序号 1-3
        """
        c2s = trial_pb2.c2s_trial_shop_buy()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        c2s.index = paramlist[2]
        return c2s

    def c2s_trial_open_jiejie(self, paramlist):
        """
        打开神秘结界
        :int trial_id: 试练副本id
        :int pos: 节点位置
        """
        c2s = trial_pb2.c2s_trial_open_jiejie()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        return c2s

    def c2s_trial_battle(self, paramlist):
        """
        杀完怪物调用
        :int trial_id: 试练副本id
        :int pos: 节点位置
        :int partner_unique_id: 出战伙伴唯一id（选填）
        :int partner_unique_id: 出战伙伴唯一id（选填）
        。。。。。。（选填）
        """
        c2s = trial_pb2.c2s_trial_battle()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        if len(paramlist) > 2:
            c2s.partner_unique_id_list.extend(paramlist[2:])
        return c2s

    def c2s_trial_exit(self, paramlist):
        """
        结束试练结算
        :int trial_id: 试练副本id
        """
        c2s = trial_pb2.c2s_trial_exit()
        c2s.trial_id = paramlist[0]
        return c2s

    def c2s_trial_reward(self, paramlist):
        """
        刷新奖励
        :int trial_id: 试练副本id
        """
        c2s = trial_pb2.c2s_trial_reward()
        c2s.trial_id = paramlist[0]
        return c2s

    def c2s_trial_use_recover(self, paramlist):
        """
        使用恢复药剂
        :int trial_id: 试练副本id
        :int id: 使用对象 主角id或者伙伴唯一id
        """
        c2s = trial_pb2.c2s_trial_use_recover()
        c2s.trial_id = paramlist[0]
        c2s.id = paramlist[1]
        return c2s

    def c2s_trial_camp_battle(self, paramlist):
        """
        试炼打怪布阵战斗
        :int trial_id: 试练副本id
        :int pos: 位置
        :int major_id: 主角ID(必填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2 - 5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        :int formation_pos: 位置ID，2 - 5(选填)
        :int partner_unique_id: 伙伴UID(选填)
        。。。。。。（选填）
        """
        c2s = trial_pb2.c2s_trial_camp_battle()
        c2s.trial_id = paramlist[0]
        c2s.pos = paramlist[1]
        c2s.formation.major_id = paramlist[2]
        partner = (len(paramlist) - 3)/2
        for i in xrange(partner):
            partner_pos = c2s.formation.partner_pos.add()
            partner_pos.partner_unique_id = paramlist[2*i+3]
            partner_pos.formation_pos = paramlist[2*i+4]
        return c2s

    def c2s_check_in_trial(self, paramlist):
        """
        登录后在试炼场景的判断，如果在，需要之后发送c2s_trial_reconnect重连
        :int in_trial: 1.在 0.不在
        """
        c2s = trial_pb2.c2s_check_in_trial()
        c2s.in_trial = paramlist[0]
        return c2s


class C2S_WONDERLAND():

    def c2s_wonderland_register(self, paramlist):
        """
        报名参与秘境副本
        :int wonderland_id: 秘境id
        :int major_id: 主角id
        :int partner_unique_id: 伙伴UID（必填）
        :int partner_unique_id: 伙伴UID（选填）
        。。。。。。（选填）
        """
        c2s = wonderland_pb2.c2s_wonderland_register()
        c2s.wonderland_id = paramlist[0]
        c2s.major_id = paramlist[1]
        if len(paramlist) > 2:
            c2s.partner_unique_id_list.extend(paramlist[2:])
        return c2s

    def c2s_wonderland_pass(self, paramlist):
        """
        领取通关奖励
        :int wonderland_id: 秘境id
        """
        c2s = wonderland_pb2.c2s_wonderland_pass()
        c2s.wonderland_id = paramlist[0]
        return c2s

    def c2s_wonderland_open_box(self, paramlist):
        """
        打开密境中的宝箱
        :int wonderland_id: 秘境id
        :int box_id: 宝箱ID
        """
        c2s = wonderland_pb2.c2s_wonderland_open_box()
        c2s.wonderland_id = paramlist[0]
        c2s.box_id = paramlist[1]
        return c2s

    def c2s_get_wonderland_list(self):
        """
        获取秘境已经通关的列表
        :param:  不需要填写参数
        """
        c2s = wonderland_pb2.c2s_get_wonderland_list()
        return c2s

class C2S_RPC():
    pass

class C2S_PROTO(C2S_ACCNAME,C2S_ACHIEVE,C2S_ACTIVE,C2S_ARENA,C2S_CHAT,C2S_COMPOSE,C2S_DRAW,C2S_DUNGEON,C2S_EXP_TRAIN,C2S_FRIEND,
                C2S_GOODS,C2S_GUDIE,C2S_MAIL,C2S_MAJOR,C2S_MCITY,C2S_PARTNER,C2S_PET,C2S_PLAYER,C2S_PVE,
                C2S_PVP,C2S_PVP_GOLOBAL,C2S_REALTIME_PVP,C2S_SHOP,C2S_SIGN,C2S_TASK,C2S_TRIAL,C2S_WONDERLAND,C2S_RPC):
    """
    全继承
    """
    pass

