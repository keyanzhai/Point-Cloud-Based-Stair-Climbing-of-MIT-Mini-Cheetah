/*! @file LegController.h
 *  @brief Common Leg Control Interface and Leg Control Algorithms
 *
 *  Implements low-level leg control for Mini Cheetah and Cheetah 3 Robots
 *  Abstracts away the difference between the SPIne and the TI Boards (the low level leg control boards)
 *  All quantities are in the "leg frame" which has the same orientation as the
 * body frame, but is shifted so that 0,0,0 is at the ab/ad pivot (the "hip
 * frame").
 */

#ifndef PROJECT_LEGCONTROLLER_H
#define PROJECT_LEGCONTROLLER_H

#include "cppTypes.h"
#include "leg_control_command_lcmt.hpp"
#include "leg_control_data_lcmt.hpp"
#include "Dynamics/Quadruped.h"
#include "SimUtilities/SpineBoard.h"
#include "SimUtilities/ti_boardcontrol.h"

/*!
 * Data sent from the control algorithm to the legs.
 */
template <typename T>
struct LegControllerCommand {
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  LegControllerCommand() { zero(); }

  // 函数功能：将结构体LegControllerCommand中所有的参数置零
  void zero();

  /* What are the meanings of each parameter? I have no clue.
    tauFeedForward: 输出的力矩（3*1）
    forceFeedFoward: 输出的力（3*1）
    qDes: 期望的关节位置（3*1）
    qdDes: 期望的关节速度（3*1）
    pDes: 期望的足端位置（3*1）    ** important **
    vDes: 期望的足端速度（3*1）
    kpCartesian: 笛卡尔空间比例系数，用来对足端行为进行控制（3*3）
    kdCartesian: 笛卡尔空间微分系数，用来对足端行为进行控制（3*3）
    kpJoint: 关节空间比例系数，用来对关节行为进行控制（3*3）
    kdJoind: 关节空间微分系数，用来对关节行为进行控制（3*3）
  */
  Vec3<T> tauFeedForward, forceFeedForward, qDes, qdDes, pDes, vDes;
  Mat3<T> kpCartesian, kdCartesian, kpJoint, kdJoint;
};

/*!
 * Data returned from the legs to the control code.
 */
template <typename T>
struct LegControllerData {
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW
  LegControllerData() { zero(); }

  void setQuadruped(Quadruped<T>& quad) { quadruped = &quad; }

  // 函数功能：将结构体LegControllerData中所有的参数置零
  void zero();

  /* What are the meanings of each parameter? I have no clue.
    q: 实际的关节位置（3*1）
    qd: 实际的关节速度（3*1）
    p: 实际的足端位置（3*1）
    v: 实际的足端速度（3*1）
    J: 关节力矩的估计值（3*1）
    tauEstimate: Jacobian矩阵（3*3）
  */
  Vec3<T> q, qd, p, v;
  Mat3<T> J;
  Vec3<T> tauEstimate;
  Quadruped<T>* quadruped;
};

/*!
 * Controller for 4 legs of a quadruped.  Works for both Mini Cheetah and Cheetah 3
 */
template <typename T>
class LegController {
 public:
  LegController(Quadruped<T>& quad) : _quadruped(quad) {
    for (auto& data : datas) data.setQuadruped(_quadruped);
  }

  void zeroCommand();
  void edampCommand(RobotType robot, T gain);
  void updateData(const SpiData* spiData);
  void updateData(const TiBoardData* tiBoardData);
  void updateCommand(SpiCommand* spiCommand);
  void updateCommand(TiBoardCommand* tiBoardCommand);
  void setEnabled(bool enabled) { _legsEnabled = enabled; };
  void setLcm(leg_control_data_lcmt* data, leg_control_command_lcmt* command);

  /*!
   * Set the maximum torque.  This only works on cheetah 3!
   */
  void setMaxTorqueCheetah3(T tau) { _maxTorque = tau; }

  LegControllerCommand<T> commands[4];
  LegControllerData<T> datas[4];
  Quadruped<T>& _quadruped;
  bool _legsEnabled = false;
  T _maxTorque = 0;
  bool _zeroEncoders = false;
  u32 _calibrateEncoders = 0;
};

template <typename T>
void computeLegJacobianAndPosition(Quadruped<T>& quad, Vec3<T>& q, Mat3<T>* J,
                                   Vec3<T>* p, int leg);

#endif  // PROJECT_LEGCONTROLLER_H
